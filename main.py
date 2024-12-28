from utils.spotify_code_generation import generate_spotify_code
from utils.image_conversion import png_to_svg_with_holes

def main():
    spotify_link = input("Enter the link for the spotify content to generate: ")
    generate_spotify_code(spotify_link, "assets/spotify_code.png")
    png_to_svg_with_holes("assets/spotify_code.png", "assets/output.svg", threshold=128)
    print("Assets generated!")

if __name__ == "__main__":
    main()