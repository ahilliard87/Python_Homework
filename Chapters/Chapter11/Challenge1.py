"""  This is the original code in the challenge

import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
FC = "airports.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
for field in fields:
    if fields.name == "NAME"
        for row in rows:
        print "Name = {0}".format(row.getValue(field.name))
"""


import arcpy
from arcpy import env
env.workspace = "C:/Users/amhill2604/Desktop/MyExcercises/Exercise07"
fc = "airports.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
for field in fields:
    if field.name == "NAME":
        for row in rows:
            print "Name = {0}".format(row.getValue(field.name))


"""
    
    Line 4: the variable FC was capitalized, it should be lower case fc.
    Line 8: the if statement was not ended with a colon(:).
    Line 8: "fields.name" was incorrect and should be "field.name"
    Line 10: the print statement was not indented properly under the last for statement

"""    
