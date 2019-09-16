import sqlite3
connection = sqlite3.connect('..\data\warm-up-DB-205.db')
cursor = connection.cursor()

def QueryNeighborhoodID(address):

    address = '\'' + address + '\''
    cursor.execute("SELECT NEIGHBORHOOD_ID FROM tblCrimes where INCIDENT_ADDRESS ='{}'".format(address))

    return_string = "The NEIGHBORHOOD_ID for that address is: " + cursor.fetchall()

    return return_string


def QueryNumCrimes(location):

    location = '\'' + location + '\'' 
    cursor.execute("SELECT COUNT(*) FROM tblCrimes WHERE NEIGHBORHOOD_ID ='{}'".format(location))
    
    return_string = "Total number of crimes in that neighborhood: " + cursor.fetchall()

    return return_string
