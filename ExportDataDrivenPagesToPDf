'''This script reads ArcGIS data driven pages, determines whether or not it should have landscape or portrait orientation
and exports it to a PDF'''

import arcpy
import re
from arcpy import env
import os.path
env.workspace = "q:\\Geodata\\shape\\vtds\\vtd2015"

sCur = arcpy.SearchCursor("q:\\Geodata\\shape\\vtds\\vtd2015\\vtd2015general.shp")

# Fetch each feature from the cursor and examine the extent properties

for row in sCur:
    #clean bad characters out of fields
    #Duplicate pct names, append county name and district for down the road processing
    ceanName = re.sub('[^\w\-_\. ]', '_', row.PCTNAME) + " +"+ row.COUNTYNAME + " +" + row.MNLEGDIST

    geom = row.shape
    ext = geom.extent

    xlength = ext.XMax - ext.XMin
    ylength = ext.YMax - ext.YMin


    if xlength > ylength:
        print"x>y, map should be landscape"
        
        #skip if the file already exists - this is a long running script so breaks happen and we have to start over
        if os.path.isfile(r"D:\\DDP Test\\Landscape\\" + str(ceanName) + ".pdf"):
            print str(ceanName) + ".pdf exists"
        else:
            print str(ceanName) + ".pdf DOES NOT exist"
        
            mxd = arcpy.mapping.MapDocument(r"q:\\Geodata\\projects\\Projects2016\\WebPrecinctMaps\\Precincts2015_10222015_landscape.mxd")
            pageID = mxd.dataDrivenPages.getPageIDFromName(str(row.PCTNAME))
            mxd.dataDrivenPages.currentPageID = pageID       
            print "Exporting landscape page {0} of {1}".format(str(mxd.dataDrivenPages.currentPageID), str(mxd.dataDrivenPages.pageCount))
            print str(row.PCTNAME) + ".pdf"
            print
            arcpy.mapping.ExportToPDF(mxd, r"D:\\DDP Test\\Landscape\\" + str(ceanName) + ".pdf",resolution=150)

            del mxd

    else:
        print"x<y, map should be portrait"

        #skip if the file already exists - this is a long running script so breaks happen and we have to start over
        if os.path.isfile(r"D:\\DDP Test\\Portrait\\" + str(ceanName) + ".pdf"):
            print str(ceanName) + ".pdf exists"
        else:
            print str(ceanName) + ".pdf DOES NOT exist"
            mxd = arcpy.mapping.MapDocument(r"q:\\Geodata\\projects\\Projects2016\\WebPrecinctMaps\\Precincts2015_10222015_portrait.mxd")
            pageID = mxd.dataDrivenPages.getPageIDFromName(str(row.PCTNAME))
            mxd.dataDrivenPages.currentPageID = pageID        
            print "Exporting portrait page {0} of {1}".format(str(mxd.dataDrivenPages.currentPageID), str(mxd.dataDrivenPages.pageCount))
            print str(row.PCTNAME) + ".pdf"
            print
            arcpy.mapping.ExportToPDF(mxd, r"D:\\DDP Test\\Portrait\\" + str(ceanName) + ".pdf",resolution=150)
            del mxd

