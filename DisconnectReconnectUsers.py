import arcpy

# Many ArcGIS SDE maintenence tasks cannot be performed while users are connected to DB
# This script will disconnect users and reconnect them after you run maintenence tasks 
# One could just comment out the AcceptConnections method to do maintenence through catalog
# then just run the accepting connections method once they are finished.

#block new connections to the database.
arcpy.AcceptConnections("Database Connections\your.sde", False)
print 'Refusing Connections'

#disconnect all users from the database.
arcpy.DisconnectUser("Database Connections\your.sde", "ALL")
print 'Disconnected all users'

# perform server maintenence here!

#Allow the database to begin accepting connections again
arcpy.AcceptConnections("Database Connections\your.sde", True)
print "Accepting connections"

