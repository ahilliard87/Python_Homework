import arcpy
from arcpy import env
env.workspace = "C:/Users/amhill2604/Desktop/Exercise06"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdescribe = arcpy.Describe(fc).shapeType
    print("{0} is {1} feature class".format(fc, fcdescribe))

