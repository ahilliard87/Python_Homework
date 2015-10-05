import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/amhill2604/FALL_2015/My_Python/Python/Data/Exercise08"

fc = "Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@"])
length = 0

for row in cursor:
    partnum = 0
    length = 0
    for part in row[0]:
        poly = arcpy.Polygon(part)
        print("Part {0} area: {1}".format(partnum, poly.area))
        print("Part {0} perimeter: {1}".format(partnum, poly.length))
        
        partnum += 1
