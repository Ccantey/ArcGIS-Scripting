# Export batch .mxds to pdf, ai, jpeg, png, emf, eps, svg, bmp, tiff, gif

# To use this script, all you have to do is set your workspace variables (line 12-13).  
# The script will export all .mxds in the directory to Illustrator, pdf, or any of the other listed formats.

# This script has hung up on very large mxd files... Usually those with large raster datasets

import arcpy, os

# Set OverWrite if files already exist
arcpy.OverWriteOutput = 1

# Set workspace variables
ws = arcpy.env.workspace = r"K:\01992-020\GIS\Maps"
outDir = r"C:\Users\ccantey\Desktop\Test"

#Select all .mxd's
mapList = arcpy.ListFiles("*.mxd")

# Export all mxds to new format
for m in mapList:
    print m
# Set any parameters as variables here, pass to arcpy.mapping.ExportToPDF(mxd, outDir + r'/' + str(m)), dataframe, colorspace)
##    data_frame = 'PAGE_LAYOUT' 
##    resolution = "300" 
##    image_quality = "NORMAL"  
##    colorspace = "RGB" 
##    compress_vectors = "True" 
##    image_compression = "DEFLATE"
##    picture_symbol = 'RASTERIZE_BITMAP'
##    convert_markers = "False"
##    embed_fonts = "True"
##    layers_attributes = "NONE"
##    georef_info = "False"
    
    mxd = arcpy.mapping.MapDocument(os.path.join(ws,m))
    arcpy.mapping.ExportToAI(mxd, outDir + r'/' + str(m)) #.ExportToPDF, .ExportToAI, etc., give it the same name as mxd
    del mxd
