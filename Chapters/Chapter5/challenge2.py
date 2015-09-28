import arcpy
from arcpy import env

env.workspace = "U:/Shared/GIS/StuData/amhill2604/FALL_2015/My_Python/Python/Data/Exercise05/Results"
arcpy.AddXY_management("hospitals.shp")
