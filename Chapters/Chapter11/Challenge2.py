""" The original code fro challenge 2

import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data\Exercise09"
raster = "landcover.tiff"
desc = arcpy.describe(raster)
x = desc.MeanCellHeight
y = desc.MeanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName
print "Cells are" + str(x) + " by " + str(y) + " " + units + "."

"""

import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise09"
raster = "landcover.tiff"
desc = arcpy.describe(raster)
x = desc.MeanCellHeight
y = desc.MeanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName
print "Cells are" + str(x) + " by " + str(y) + " " + units + "."


"""

    Line 3: The backspaces in the path name setting workspace should all be forward slashes
    Line 4: .tiff is not a valid file type, the proper ending shouild be .tif
    Line 5: the .Describe method is suppose to be capitalized
    Line 6: Mean in desc.MeanCellHeight statement should be lowercase
    Line 7: Mean in desc.MeanCellWidth statement should be lowercase
    Line 8: spatial in desc.spatialReference shoule be capitalized to Spatial.

"""
