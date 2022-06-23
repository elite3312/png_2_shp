# Name: RasterToPolygon_Ex_02.py
# Description: Converts a raster dataset to polygon features.
# Requirements: None

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
#env.workspace = "C:/Users/user/Documents/ArcGIS/Default.gdb"
env.workspace="."

# Set local variables
inRaster = "TH_Fold1_REAL TEST SA2_IMG1_Post10"
outPolygons = "./zones.shp"
#field = "VALUE"

# Execute RasterToPolygon
arcpy.RasterToPolygon_conversion(inRaster, outPolygons, "NO_SIMPLIFY", )