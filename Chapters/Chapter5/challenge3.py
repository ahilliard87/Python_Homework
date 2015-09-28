import arcpy

arcpy.env.workspace = "U:/Shared/GIS/StuData/amhill2604/FALL_2015/My_Python/Python/Data/Exercise05/Results"
outputClass = "U:/Shared/GIS/StuData/amhill2604/FALL_2015/My_Python/Python/Data/Exercise05/Results/parks_diss.shp"
arcpy.Dissolve_management("parks.shp", outputClass, "PARK_TYPE", "", "SINGLE_PART", "")
