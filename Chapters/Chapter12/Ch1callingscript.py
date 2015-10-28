import arcpy
from arcpy import env
env.workspace = "C:/Users/amhill2604/Desktop/MyExcercises/MyEx12"
import mycount

print(mycount.countstringfields("streets.shp"))
