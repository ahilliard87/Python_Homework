import arcpy
from arcpy import env
env.workspace = "C:/Users/amhill2604/Desktop/MyExcercises/MyEx12"

def countstringfields(feat):
    """ This function determines the numbers of fields of type string in an input
        feature class.
    """
    
    fields = arcpy.ListFields (feat)
    count = 0
    for field in fields:
        if field.type == "String":
            count += 1
        return count
