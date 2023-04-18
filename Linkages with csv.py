#Author-
#Description-

import csv 
import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:       
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        document = adsk.core.Document.cast(app.activeDocument)
        

        rootComp = design.rootComponent
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)
        circles = sketch.sketchCurves.sketchCircles
        lines = sketch.sketchCurves.sketchLines
        arcs = sketch.sketchCurves.sketchArcs
        extrudes = rootComp.features.extrudeFeatures 

        with open("C:\\Users\\Alexandra Valdepeñas\\Desktop\\Linkagestrial.csv", 'r') as file:
            csvreader = csv.reader(file, dialect='excel')
            for row in csvreader:
                list = row
                #SKetches the two circles for every linkage
                circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(float(list[1]), float(list[2]), float(list[17])), 6.3)
                circle2 = circles.addByCenterRadius(adsk.core.Point3D.create(float(list[3]), float(list[4]), float(list[17])), 6.3)

                #sketches edges of joints
                point0 = adsk.core.Point3D.create(float(list[5]), float(list[6]), float(list[17]))
                point1 = adsk.core.Point3D.create(float(list[7]), float(list[8]), float(list[17]))
                point2 = adsk.core.Point3D.create(float(list[9]), float(list[10]), float(list[17]))
                point3 = adsk.core.Point3D.create(float(list[11]), float(list[12]), float(list[17]))    
                lines.addByTwoPoints(point0, point2)
                lines.addByTwoPoints(point1, point3)

                #sketches arcs at the ends
                pointarc1 = adsk.core.Point3D.create(float(list[13]), float(list[14]), float(list[17]))
                pointarc2 = adsk.core.Point3D.create(float(list[15]), float(list[16]), float(list[17]))
                arc1 = arcs.addByThreePoints(point0, pointarc1, point1)
                arc2 = arcs.addByThreePoints(point2, pointarc2, point3)

                #extrudes 
                profile = sketch.profiles.item(2)
                ext_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                distance = adsk.core.ValueInput.createByReal(5.5)
                ext_input.setDistanceExtent(False, distance)
                ext_input.isSolid = True
                extrudes.add(ext_input)
                ui.messageBox(list[0])


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
