#Exercise 9

import arcpy
from arcpy import env
env.workspace = r"D:\School\GradSchool\ClassWork\Spring2017\GIS_5990_Python\Homework\Week9\Exercise09\Exercise09"
##rasterlist = arcpy.ListRasters()
##for raster in rasterlist:
##    print raster

##raster = "tm.img"
##desc = arcpy.Describe(raster)
##print "Raster base name is: " + desc.basename
##print "Raster data type is: " + desc.dataType
##print "Raster file etension is: " + desc.extension
##print "Raster spatial reference is: " + desc.spatialReference.name
##print "Raster format is: " + desc.format
##print "Raster compression type is: " + desc.compressionType
##print "Raster number of bands is: " + str(desc.bandCount)

##raster = "landcover.tif"
##desc = arcpy.Describe(raster)
##print "Raster base name is: " + desc.basename
##print "Raster data type is: " + desc.dataType
##print "Raster file etension is: " + desc.extension
##print "Raster spatial reference is: " + desc.spatialReference.name
##print "Raster format is: " + desc.format
##print "Raster compression type is: " + desc.compressionType
##print "Raster number of bands is: " + str(desc.bandCount)

rasterband = "tm.img/Layer_1"
desc = arcpy.Describe(rasterband)
x = desc.meanCellHeight
y = desc.meanCellWidth
spatialref = desc.spatialReference
units = spatialref.angularUnitName
print "The raster resolution of Band 1 is " + str(x) + " by " + str(y) + " " + units + "."

