import arcpy
from arcpy import env

shortpath = "C:/Users/amhill2604/Desktop/MyExercise09"
env.workspace = shortpath
rasterlist = arcpy.ListRasters()
arcpy.CreatePersonalGDB_management(shortpath + "/Results", "myrasters.gdb")

for raster in rasterlist:
    desc = arcpy.Describe(raster)
    rname = desc.baseName
    outraster = shortpath + "/Results/myrasters.gdb/" + rname
    arcpy.CopyRaster_management(raster, outraster)
