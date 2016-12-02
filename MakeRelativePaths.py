import arcpy, os

#walk through all subdirectories and change mxd to store relative paths

for root, dirs, files in os.walk(r"Q:\Geodata\shape"):
        for f in files:
            if f.endswith(".mxd"):
                filepath = root + '\\' + f
                print filepath
                try:
                    mxd = arcpy.mapping.MapDocument(filepath)
                    #set relative paths property
                    mxd.relativePaths = True
                    mxd.save()
                except:
                    print filepath + ' failed'
                    pass

                

