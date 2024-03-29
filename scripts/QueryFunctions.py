import sqlite3

connection = sqlite3.connect('../data/warm-up-DB-205.db')
cursor = connection.cursor()

userInput = {"incident id": "fld_incident_id",
             "incident": "fld_incident_id",
             "offense id": "fld_offense_id",
             "offense": "fld_offense_id",
             "occurred": "fld_first_occurence_date",
             "date": "fld_first_occurence_date",
             "time": "fld_first_occurence_date",
             "first occurrence": "fld_first_occurence_date",
             "first occurred": "fld_first_occurence_date",
             "reported date": "fld_reported_date",
             "reported": "fld_reported_date",
             "incident address": "fld_incident_address",
             "address": "fld_incident_address",
             "location": "fld_incident_address",
             "precinct id": "fld_precinct_id",
             "precinct": "fld_precinct_id",
             "neighborhood id": "fld_neighborhood_id",
             "neighborhood": "fld_neighborhood_id",
             "offense code": "fld_offense_code",
             "code": "fld_offense_code",
             "offense name": "fld_offense_type",
             "name": "fld_offense_type",
             "crimes": "fld_offense_type",
             "offense category": "fld_offense_category",
             "crime": "fld_is_crime",
             "is crime": "fld_is_crime",
             "traffic": "fld_is_traffic",
             "is traffic": "fld_is_traffic"}


def QueryTop10(key, column, return_column):
    key = '\'' + key + '\''  # pad key with quotes to ensure dashes, spaces, and underscores are included
    tbl_column = userInput[column]
    tbl_return_column = userInput[return_column]
    # Get only addresses from tblCrimes table with neighborhood ID
    cursor.execute('SELECT {rc}, COUNT({rc}) '
                   'FROM tblCrimes '
                   'LEFT JOIN tblOffenseCode USING(fld_offense_code) '
                   'WHERE {cl}={ky} '
                   'GROUP BY {rc} ORDER '
                   'BY COUNT({rc}) DESC LIMIT 10'.format(cl=tbl_column, ky=key, rc=tbl_return_column))
    row = cursor.fetchall()
    return_string = ""

    if row:
        for item in row:
            if item[0] != "":  # Throw away blank lines
                return_string += item[0] + " -- "
                return_string += str(item[1]) + " Occurrence(s)"
                return_string += "\n"
    else:  # Throw warning that searched key doesn't exist
        return_string += '{ky} does not exist. Try again with a different key.'.format(ky=key)

    return return_string


def QueryNumCrimes(key, column):
    key = '\'' + key + '\''
    tbl_column = userInput[column]
    cursor.execute('SELECT COUNT(*) FROM tblCrimes '
                   'LEFT JOIN tblOffenseCode USING(fld_offense_code) '
                   'WHERE {cl}={ky}'.format(cl=tbl_column, ky=key))

    return_string = "Total number of crimes in {ky}: ".format(ky=key) + str(cursor.fetchone()[0])

    return return_string


def QueryOne(key, column, return_column):
    key = '\'' + key + '\''
    tbl_column = userInput[column]
    tbl_return_column = userInput[return_column]
    cursor.execute('SELECT {rc} FROM tblCrimes '
                   'LEFT JOIN tblOffenseCode USING(fld_offense_code)'
                   'where {cl}={ky}'.format(cl=tbl_column, ky=key, rc=tbl_return_column))

    return_string = "The {rc} for that {cl} is: ".format(cl=column, rc=return_column) + cursor.fetchone()[0]

    return return_string

def dbKey():
    db_key = ''
    for key in userInput:
        db_key +=  key + ', '
        
    return db_key