import arcpy
from arcpy import env
env.workspace = "C:/Users/amhill2604/Desktop/Exercise07"
fc = "airports.shp"

unique_name = arcpy.CreateUniqueName("Results/airport_buff.shp")
unique_name2 = arcpy.CreateUniqueName("Results/seaplane_buff.shp")

arcpy.Buffer_analysis(fc, unique_name, "15000 METERS",)
arcpy.Buffer_analysis(fc, unique_name2, "7500 METERS",)
