import sqlite3
connection = sqlite3.connect('..\data\warm-up-DB-205.db')
cursor = connection.cursor()

def QueryTop10(key, column, return_column):
    key = '\'' + key + '\'' # pad key with quotes to ensure dashes, spaces, and underscores are included
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

def QueryNumCrimes(location):
    return False


str = QueryTop10('goldsmith', 'fld_neighborhood_id', 'fld_offense_type')
print(str)
