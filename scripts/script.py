import dbCreate
import QueryFunctions as q
k = 'speer'
c ='fld_neighborhood_id'

dbCreate.connect_database()
d = q.QueryNumCrimes(k,c)
print(d)

def parse_query(input_string):
    string_list = input_string.split()
    # top return_column in column : key
    start = string_list.pop(0)
    if start == 'top':
        return_column = read_until('in')
        column = read_until(':')
        key = read_until()
        if key == '':
        elif column == '':
        elif return_column == '':
            return 'Invalid'
        else:
            return q.QueryTop10(key, column, return_column)
    # crimes in column : key
    elif start == 'crimes':
    # x at column : key
    elif start in

def read_until(end_str):
    return ''