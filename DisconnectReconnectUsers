import arcpy

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

