import cv2
import svgwrite
import numpy as np

def png_to_svg_with_holes(png_path, svg_path, threshold=128, 
                          min_contour_area=50, morph_kernel_size=3):
    """
    Converts a PNG to an SVG, preserving holes by combining parent and child
    contours into one <path> element with fill-rule="evenodd".
    Also removes small noise via morphological opening & area filtering.
    """
    # 1) Read grayscale
    gray = cv2.imread(png_path, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        raise ValueError(f"Could not read image from {png_path}")
    
    # 2) Optional: Light smoothing to reduce noise
    # gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # 3) Threshold
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # 4) Morphological opening to remove small white specks
    kernel = np.ones((morph_kernel_size, morph_kernel_size), np.uint8)
    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    
    # 5) Find contours with hierarchy
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if hierarchy is None:
        raise ValueError("No contours found. Try adjusting threshold or check your image.")
    
    # 6) Create the SVG canvas
    dwg = svgwrite.Drawing(svg_path, profile='tiny')
    
    def contour_to_path_string(idx):
        pts = contours[idx].reshape(-1, 2)
        if len(pts) == 0:
            return ""
        return "M " + " L ".join(f"{p[0]},{p[1]}" for p in pts) + " Z"
    
    visited = set()
    
    # 7) Build compound paths from top-level contours
    for i in range(len(contours)):
        parent = hierarchy[0][i][3]
        
        # Check area filter (skip small junk)
        if cv2.contourArea(contours[i]) < min_contour_area:
            continue
        
        if parent == -1:  # top-level
            compound_path = []
            stack = [i]
            while stack:
                idx = stack.pop()
                
                if idx not in visited:
                    visited.add(idx)
                    # Also skip if it's below the area threshold
                    if cv2.contourArea(contours[idx]) >= min_contour_area:
                        compound_path.append(contour_to_path_string(idx))
                    
                    # Gather child contours
                    child_idx = hierarchy[0][idx][2]
                    while child_idx != -1:
                        stack.append(child_idx)
                        child_idx = hierarchy[0][child_idx][0]
            
            # Join sub-paths, add fill_rule="evenodd"
            if compound_path:
                full_path = " ".join(compound_path)
                dwg.add(
                    dwg.path(
                        d=full_path,
                        fill="black",
                        stroke="black",
                        stroke_width=1,
                        fill_rule="evenodd"
                    )
                )
    
    # 8) Save
    dwg.save()
    print(f"SVG saved to: {svg_path}")


# Example usage
if __name__ == "__main__":
    png_to_svg_with_holes("assets/spotify_code.png", "assets/output.svg", threshold=128)
