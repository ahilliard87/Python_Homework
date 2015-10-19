import arcpy
from arcpy import sa
from arcpy import env

env.workspace = "C:/Users/amhill2604/Desktop/MyExercise09"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")

elevraster = arcpy.Raster("elevation")
lcraster = arcpy.Raster("landcover.tif")

slope = arcpy.sa.Slope(elevraster)
aspect = arcpy.sa.Aspect(elevraster)
modslope = ((slope > 5) & (slope < 20))
southaspect = ((aspect > 150) & (aspect < 270))
forestcov = ((lcraster == 41) |(lcraster == 42) | (lcraster ==43))

finalraster = (modslope & southaspect & forestcov)
finalraster.save("finalraster.tif")
