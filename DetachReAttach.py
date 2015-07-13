import csv
import arcpy
import os
import sys

input = r"Database Connections\your.sde\pictures featureclass"
inputField = "NAME"
matchTable = r"C:\Users\<user>\Desktop\matchtable.csv"
matchField = "NAME"
pathField = r"picture Location" 
rootdir = r"C:\Root Directory\A-Z pictures\picture"
#get subdirectories
subdirectories = [x[0] for x in os.walk(rootdir)]

for folders in subdirectories[1:]:
    print folders
    try:
        # create a new Match Table csv file
        writer = csv.writer(open(matchTable, "wb"), delimiter=",")

        # write a header row (the table will have two columns: ParcelID and Picture)
        writer.writerow([matchField, pathField])

        # iterate through each picture in the directory and write a row to the table
        for file in os.listdir(folders):
            if str(file).find(".pdf") > -1:
                writer.writerow([str(file).replace(".pdf", ""), file])

        # the input feature class must first be GDB attachments enabled
        # arcpy.EnableAttachments_management(input)

        # use the match table with the Remove Attachments tool
        arcpy.RemoveAttachments_management(input, inputField, matchTable, matchField, pathField)

        # use the match table with the Add Attachments tool
        arcpy.AddAttachments_management(input, inputField, matchTable, matchField, pathField, folders)
        print "Finished Attaching Documents in " + folders
        
    except:
        print arcpy.GetMessages(2)
