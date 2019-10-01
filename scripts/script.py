import dbCreate
import QueryFunctions as q


def read_until(read_list, end_str):
    return_string = ''
    while read_list and read_list[0] != end_str:
        return_string += read_list[0] + ' '
        del read_list[0]
    if read_list and read_list[0] == end_str:
        del read_list[0]
    return return_string.strip()


def parse_query(input_string):
    string_list = input_string.split()
    # top return_column in column : key
    start = string_list.pop(0)
    if start == 'top':
        return_column = read_until(string_list, 'in')
        column = read_until(string_list, ':')
        key = read_until(string_list, '')
        print(return_column)
        if return_column not in q.userInput:
            return 'Return column does not exist or there is no \'in\'  statement'
        elif column not in q.userInput:
            return 'Column does not exist or there is no \'in\'  statement'
        elif key == '':
            return 'There is no \':\' after the column or no key was entered'
        else:
            return q.QueryTop10(key, q.userInput[column], q.userInput[return_column])
    # crimes in column : key
    elif start == 'crimes':
        junk = read_until(string_list, 'in')
        column = read_until(string_list, ":")
        key = read_until(string_list, '')
        if column not in q.userInput:
            return 'Column does not exist or there is no \':\'  statement'
        elif key == '':
            return 'There is no \':\' after the column or no key was entered'
        else:
            return q.QueryNumCrimes(key, q.userInput[column])
    # x at column : key
    elif start in q.userInput:
        return_column = start
        junk = read_until(string_list, 'at')
        column = read_until(string_list, ':')
        key = read_until(string_list, '')
        if column not in q.userInput:
            return 'Column does not exist or there is no \':\'  statement'
        elif key == '':
            return 'There is no \':\' after the column or no key was entered'
        else:
            return q.QueryNumCrimes(key, q.userInput[column])
    else:
        return 'Data request must start with \'top\', \'crimes\', or a column name'


dbCreate.connect_database()
print(parse_query('top offense name in neighborhood : speer'))
