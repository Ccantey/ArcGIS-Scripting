import arcpy
import os

##This program appends (copies) feature classes from another agencies geodatabase
##into our agency's geodatabase. Must first truncate data, then append.
##This program assumes matching schema. Workaround would be to use field_mapping parameter.
##This program uses desktop copies of gdb's for proof of concept
##This program calls the Append_management method 10 times. A loop using ListFeatureClasses() method would work


##Read Water Database
arcpy.env.workspace = "C:\Users\ccantey\Desktop\Local Government.gdb\WaterDistribution" ##works

datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

##Truncate all feature classes in current water distributin feature dataset
try:
  for ds in datasets:
      for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
          path = os.path.join(arcpy.env.workspace, ds, fc)
          ## Print all the feature classes
          print path, " truncated"
          arcpy.TruncateTable_management(path)
except:
    print "didnt't work"
    print arcpy.GetMessages()


# Set local variables
inLocation = "C:\Users\ccantey\Desktop\Water_GISDATA\WaterSystem.mdb\Water_Distribution_Network"
outLocation = "C:\Users\ccantey\Desktop\Local Government.gdb"
schemaType = "NO_TEST"
fieldMappings = ""
subtype = ""

print ""

try:
    # Process: Append the feature classes into the empty feature class   
    wLateralLine = [inLocation + "\wLateralLine"]    
    arcpy.Append_management(wLateralLine, outLocation + "\wLateralLine", schemaType, fieldMappings, subtype)
    print "pass wLateralLine"
    
    # Process: Append the feature classes into the empty feature class   
    wControlValve = [inLocation + "\wControlValve"]    
    arcpy.Append_management(wControlValve, outLocation + "\wControlValve", schemaType, fieldMappings, subtype)
    print "pass wControlValve"

    # Process: Append the feature classes into the empty feature class   
    wBreaks = [inLocation + "\wBreaks"]    
    arcpy.Append_management(wBreaks, outLocation + "\wBreaks", schemaType, fieldMappings, subtype)
    print "pass wBreaks"

    # Process: Append the feature classes into the empty feature class   
    wPressurizedMain = [inLocation + "\wPressurizedMain"]    
    arcpy.Append_management(wControlValve, outLocation + "\wPressurizedMain", schemaType, fieldMappings, subtype)
    print "pass wPressurizedMain"

    # Process: Append the feature classes into the empty feature class   
    wFitting = [inLocation + "\wFitting"]    
    arcpy.Append_management(wFitting, outLocation + "\wFitting", schemaType, fieldMappings, subtype)
    print "pass wFitting"

    # Process: Append the feature classes into the empty feature class   
    wHydrant = [inLocation + "\wHydrant"]    
    arcpy.Append_management(wHydrant, outLocation + "\wHydrant", schemaType, fieldMappings, subtype)
    print "pass wHydrant"

    # Process: Append the feature classes into the empty feature class   
    wManhole = [inLocation + "\wManhole"]    
    arcpy.Append_management(wManhole, outLocation + "\wManhole", schemaType, fieldMappings, subtype)
    print "pass wManhole"

    # Process: Append the feature classes into the empty feature class   
    wNetworkStructure = [inLocation + "\wNetworkStructure"]    
    arcpy.Append_management(wNetworkStructure, outLocation + "\wNetworkStructure", schemaType, fieldMappings, subtype)
    print "pass wNetworkStructure"

    # Process: Append the feature classes into the empty feature class   
    wSystemValve = [inLocation + "\wSystemValve"]    
    arcpy.Append_management(wSystemValve, outLocation + "\wSystemValve", schemaType, fieldMappings, subtype)
    print "pass wSystemValve"

    # Process: Append the feature classes into the empty feature class   
    Water_Distribution_Network_Junctions = [inLocation + "\Water_Distribution_Network_Junctions"]    
    arcpy.Append_management(Water_Distribution_Network_Junctions, outLocation + "\Water_Distribution_Network_Junctions", schemaType, fieldMappings, subtype)
    print "pass Water_Distribution_Network_Junctions"

except:
    # If an error occurred while running a tool print the messages
    print arcpy.GetMessages()

