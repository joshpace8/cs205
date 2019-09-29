import sqlite3

connection = sqlite3.connect('../data/warm-up-DB-205.db')
cursor = connection.cursor()

userInput = {"incident id": "INCIDENT_ID",
             "incident": "INCIDENT_ID",
             "offense id": "OFFENSE_ID",
             "offense": "OFFENSE_ID",
             "occurred": "FIRST_OCCURRENCE_DATE",
             "date": "FIRST_OCCURRENCE_DATE",
             "time": "FIRST_OCCURRENCE_DATE",
             "first occurrence": "FIRST_OCCURRENCE_DATE",
             "first occurred": "FIRST_OCCURRENCE_DATE",
             "reported date": "REPORTED_DATE",
             "reported": "REPORTED_DATE",
             "incident address": "INCIDENT_ADDRESS",
             "address": "INCIDENT_ADDRESS",
             "location": "INCIDENT_ADDRESS",
             "precinct id": "PRECINCT_ID",
             "precinct": "PRECINCT_ID",
             "neighborhood id": "NEIGHBORHOOD_ID",
             "neighborhood": "NEIGHBORHOOD_ID",
             "offense code": "OFFENSE_CODE",
             "code": "OFFENSE_CODE",
             "offense name": "OFFENSE_TYPE_NAME",
             "offense category": "OFFENSE_CATEGORY_NAME",
             "crime": "IS_CRIME",
             "is crime": "IS_CRIME",
             "traffic": "IS_TRAFFIC",
             "is traffic": "IS_TRAFFIC"}

def QueryTop10(key, column, return_column):
    key = '\'' + key + '\''  # pad key with quotes to ensure dashes, spaces, and underscores are included
    # Get only addresses from tblCrimes table with neighborhood ID
    cursor.execute('SELECT {rc}, COUNT({rc}) '
                   'FROM tblCrimes '
                   'LEFT JOIN tblOffenseCode USING(fld_offense_code) '
                   'WHERE {cl}={ky} '
                   'GROUP BY {rc} ORDER '
                   'BY COUNT({rc}) DESC LIMIT 10'.format(cl=column, ky=key, rc=return_column))
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


def QueryNumCrimes(key, column):
    key = '\'' + key + '\''
    cursor.execute('SELECT COUNT(*) FROM tblCrimes '
                   'LEFT JOIN tblOffenseCode USING(fld_offense_code) '
                   'WHERE {cl}={ky}'.format(cl=column, ky=key))

    return_string = "Total number of crimes in {ky}: ".format(ky=key) + str(cursor.fetchall())

    return return_string


def QueryOne(key, column, return_column):
    key = '\'' + key + '\''
    cursor.execute('SELECT {rc} FROM tblCrimes '
                   'LEFT JOIN tblOffenseCode USING(fdl_offense_code)'
                   'where {cl}={ky}'.format(cl=column, ky=key, rc=return_column))

    return_string = "The {rc} for that {cl} is: ".format(cl=column, rc=return_column) + cursor.fetchall()

    return return_string
