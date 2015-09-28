import os.path
import arcpy
from arcpy import env
env.workspace = "C:/Users/amhill2604/Desktop/Exercise06"

if not os.path.isdir(env.workspace + "/Results/mydb.gdb"):
    print ("Creating File GDB")
    arcpy.CreateFileGDB_management("C:/Users/amhill2604/Desktop/Exercise06/Results", "NM.gdb")


env.workspace = "C:/Users/amhill2604/Desktop/Exercise06/Results/NM.gdb"
print("Copying Features")
for feature in arcpy.ListFeatureClasses():
    dataset = arcpy.Describe(feature)
    if dataset.shapeType == "Polygon":
        arcpy.CopyFeatures_management(feature, "C:/Users/amhill2604/Desktop/Exercise06/Results/mydb.gdb/" + dataset.name)
        


