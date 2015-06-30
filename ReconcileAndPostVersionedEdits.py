import arcpy, time, smtplib, random


# get a list of connected users.
userList = arcpy.ListUsers("Database Connections/###.sde")

# get a list of usernames of users currently connected and make email addresses
emailList = [user.Name for user in arcpy.ListUsers("Database Connections/###.sde")]
filteredEmail = []
for users in  emailList:
    try:
      #print users.split('\\',1)[1].split('"',1)[0] + "@###.org"
      if users.split('\\',1)[1].split('"',1)[0] == 'ARCGIS':
          #do not mail to 'ARCGIS' user (web services)
          pass
      else:
        filteredEmail =  users.split('\\',1)[1].split('"',1)[0] + "@####.org"
    except:
        #do not mail to 'DBO' user (me)
      pass

print filteredEmail    
# take the email list and use it to send an email to connected users.
SERVER = "Your mail server"
FROM = "SDE Admin <ccantey@####>"
TO = filteredEmail
SUBJECT = "Maintenance is about to be performed"
MSG = "Auto generated Message.\n\rGIS: Server maintenance will be performed in 5 minutes, please save all edits and maps. \nReconciling and posting all edited versions of ####.sde. \n\nPlease log off of all ArcGIS applications."

# Prepare actual message
MESSAGE = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, MSG)

# Send the mail if filteredEmail
try:
    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, MESSAGE)
    server.quit()
except:
    pass


try:
    #Weekly synchronization of County parcels
    arcpy.SynchronizeChanges_management("GIS Servers/gis on #### (user)/GeoData/####y_GeoData.GeoDataServer","DBO.####sParcels","Database Connections/####.sde","FROM_GEODATABASE1_TO_2","IN_FAVOR_OF_GDB1","BY_OBJECT","DO_NOT_RECONCILE")
    print 'Synchronized parcels from County'
    
    #block new connections to the database.
    arcpy.AcceptConnections('Database Connections/###.sde', False)

    # wait 10 minutes
    time.sleep(300)

    #disconnect all users from the database.
    arcpy.DisconnectUser('Database Connections/###.sde', "ALL")

    #reconcile users to QC
    arcpy.ReconcileVersions_management("Database Connections/###.sde","ALL_VERSIONS","DBO.QC","DBO.Chris;DBO.Joe;DBO.Kraig;DBO.Marc;DBO.Adam","LOCK_ACQUIRED","NO_ABORT","BY_OBJECT","FAVOR_EDIT_VERSION","POST","KEEP_VERSION","#")
    print 'reconciled & posted users to QC'

    #reconcile QC to DEFAULT
    arcpy.ReconcileVersions_management("Database Connections/###.sde","ALL_VERSIONS","dbo.DEFAULT","DBO.QC","LOCK_ACQUIRED","NO_ABORT","BY_OBJECT","FAVOR_TARGET_VERSION","POST","KEEP_VERSION","c:/temp/reconcilelog.txt")
    print 'reconciled & posted QC to DEFAULT'

    #compress database
    arcpy.Compress_management('Database Connections/###.sde')
    print 'DB compressed'

    #Allow the database to begin accepting connections again
    arcpy.AcceptConnections('Database Connections/###.sde', True)


    # Email GIS Admin when task is accomplished.
    SERVER = "Your mail server"
    FROM = "SDE Admin <ccantey@####>"
    TO = "SDE Admin <ccantey@####>"
    SUBJECT = "Maintenance was performed"
    MSG = "Auto generated Message.\n\rGIS: Server maintenance was performed. \nReconciled and posted all edited versions of ####.sde. \n\nPlease delete the log file located in C-Temp folder ."

    # Prepare actual message
    MESSAGE = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, MSG)

    # Send the mail if script is successful
    try:
        server = smtplib.SMTP(SERVER)
        server.sendmail(FROM, TO, MESSAGE)
        server.quit()
    except:
        pass
except:
        # Email GIS Admin if task fails.
    SERVER = "Your mail server "
    FROM = "SDE Admin <ccantey@####>"
    TO = "SDE Admin <ccantey@####>"
    SUBJECT = "An error occured."
    MSG = "Auto generated Message.\n\rGIS: Server maintenance was NOT performed. \nAn error occured while reconciling and posting edited versions of OS@###.sde. \n\nThis most likely occured because this sript does not overwrite the previous reconcil log. Please delete the log file located in C-Temp folder ."

    # Prepare actual message
    MESSAGE = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, MSG)

    # Send the mail if script is successful
    try:
        server = smtplib.SMTP(SERVER)
        server.sendmail(FROM, TO, MESSAGE)
        server.quit()
    except:
        pass

