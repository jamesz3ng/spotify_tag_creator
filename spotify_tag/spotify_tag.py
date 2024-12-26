import adsk.core
import adsk.fusion
import traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Hello script')

        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            ui.messageBox("A Fusion design must be active.")
            return

        root_comp = design.rootComponent
        sketches = root_comp.sketches

        # 1) Create & Extrude a rectangle on the XY plane
        xy_plane = root_comp.xYConstructionPlane
        rect_sketch = sketches.add(xy_plane)
        
        lines = rect_sketch.sketchCurves.sketchLines
        p1 = adsk.core.Point3D.create(0, 0, 0)
        p2 = adsk.core.Point3D.create(8.5, 0, 0)
        p3 = adsk.core.Point3D.create(8.5,2, 0)
        p4 = adsk.core.Point3D.create(0, 2, 0)
        
        lines.addByTwoPoints(p1, p2)
        lines.addByTwoPoints(p2, p3)
        lines.addByTwoPoints(p3, p4)
        lines.addByTwoPoints(p4, p1)

        if rect_sketch.profiles.count == 0:
            ui.messageBox("No closed profile found. Cannot extrude.")
            return

        rect_profile = rect_sketch.profiles.item(0)
        extrudes = root_comp.features.extrudeFeatures
        ext_input = extrudes.createInput(
            rect_profile, 
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )

        distance = adsk.core.ValueInput.createByString("2.75 mm")
        ext_input.setDistanceExtent(False, distance)
        extrude_feature = extrudes.add(ext_input)

        # 2) Create a new sketch on the *top face* of that extrusion
        top_face = extrude_feature.endFaces[0]
        svg_sketch = sketches.add(top_face)

        # 3) Set up the SVG import
        import_manager = app.importManager
        svg_file_path = "/Users/jameszeng/Documents/Projects/spotify_tag_creator/assets/output.svg"
        svg_import_options = import_manager.createSVGImportOptions(svg_file_path)
        
        # Point the import at the new top-face sketch
        svg_import_options.targetBaseOrSketch = svg_sketch

        # Create a matrix and do both translation & scale
        transform = adsk.core.Matrix3D.create()
        
        # Set a uniform scale factor (e.g., 0.5 = 50%)
        scale_factor = 0.5
        transform.setCell(0, 0, scale_factor)  # X scale - negative scale factor for mirroring across the axis
        transform.setCell(1, 1, scale_factor)  # Y scale
        transform.setCell(2, 2, scale_factor)  # Z scale - not used
        
        # Shift the sketch down for hole
        translate_vec = adsk.core.Vector3D.create(0.2, 0, 0)
        transform.translation = translate_vec
        
        svg_import_options.transform = transform

        # 4) Import the SVG into the top sketch
        import_manager.importToTarget(svg_import_options, svg_sketch)

        svg_profiles = svg_sketch.profiles
        count_svg_profiles = svg_profiles.count

        # new_profile = svg_profiles.item(24)

        for i in range(1, 25):
            prof = svg_profiles.item(i)
            extrudes = root_comp.features.extrudeFeatures
            new_ext_input = extrudes.createInput(
                prof,
                adsk.fusion.FeatureOperations.NewBodyFeatureOperation
            )

            distance_val = adsk.core.ValueInput.createByString("1 mm")
            new_ext_input.setDistanceExtent(False, distance_val)
            extrudes.add(new_ext_input)

        ui.messageBox("Extruded the first SVG profile by 1 mm.")

        ui.messageBox(f"SVG Sketch has {count_svg_profiles} profile(s).")

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
