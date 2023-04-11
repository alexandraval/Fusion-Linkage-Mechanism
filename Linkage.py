#Author- Alexandra Valdepeñas
#Description- Create a linkage given input length

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)
        circles = sketch.sketchCurves.sketchCircles
        circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), .63)
        circle2 = circles.addByCenterRadius(adsk.core.Point3D.create(7, 0, 0), .63)
        point0 = adsk.core.Point3D.create(0, 0.93, 0)
        point1 = adsk.core.Point3D.create(0, -0.93, 0)
        point2 = adsk.core.Point3D.create(7, 0.93, 0)
        point3 = adsk.core.Point3D.create(7, -0.93, 0)
        pointarc1 = adsk.core.Point3D.create(-0.93, 0, 0)
        pointarc2 = adsk.core.Point3D.create(7.93, 0, 0)
        lines = sketch.sketchCurves.sketchLines     
        lines.addByTwoPoints(point0, point2)
        lines.addByTwoPoints(point1, point3)
        arcs = sketch.sketchCurves.sketchArcs
        arc1 = arcs.addByThreePoints(point0, pointarc1, point1)
        arc2 = arcs.addByThreePoints(point2, pointarc2, point3)
        profile = sketch.profiles.item(2)
        extrudes = rootComp.features.extrudeFeatures
        ext_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(0.55)
        ext_input.setDistanceExtent(False, distance)
        ext_input.isSolid = True
        extrudes.add(ext_input)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
