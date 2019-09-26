import sqlite3
connection = sqlite3.connect('..\data\warm-up-DB-205.db')
cursor = connection.cursor()

def QueryAdresses(key, column):
    key = '\'' + key + '\'' # pad key with quotes to ensure dashes, spaces, and underscores are included
    # Get only addresses from tblCrimes table with neighborhood ID
    cursor.execute('SELECT INCIDENT_ADDRESS, COUNT(INCIDENT_ADDRESS) FROM tblCrimes where {cl}={ky} GROUP BY INCIDENT_'
                   'ADDRESS ORDER BY COUNT(INCIDENT_ADDRESS) DESC LIMIT 10'.format(cl=column, ky=key))
    row = cursor.fetchall()
    return_string = ""

    if row:
        for item in row:
            if item[0] != "":  # Throw away blank addresses
                return_string += item[0] + " -- "
                return_string += str(item[1]) + " Occurrence(s)"
                return_string += "\n"
    else:  # Throw warning that searched neighborhood doesn't exist
        return_string += 'That neighborhood does not exist. Try again with a different Neighborhood.'

    return return_string

def QueryNumCrimes(location):
    return False

def QueryCommonCrimes(location):
    return False


str = QueryAdresses('jefferson-park', 'NEIGHBORHOOD_ID')
print(str)
