import dbCreate
import QueryFunctions as q


def read_until(read_list, end_str):
    return_string = ''
    while read_list and read_list[0] != end_str:
        return_string += read_list[0] + ' '
        del read_list[0]
    if read_list and read_list[0].lower() == end_str:
        del read_list[0]
    return return_string.strip()


def parse_query(input_string):
    string_list = input_string.split()
    # top return_column in column : key
    start = string_list.pop(0).lower()
    if start == 'top':
        return_column = read_until(string_list, 'in').lower()
        column = read_until(string_list, ':').lower()
        key = read_until(string_list, '')
        if return_column not in q.userInput:
            return 'Return column does not exist or there is no \'in\'  statement'
        elif column not in q.userInput:
            return 'Column does not exist or there is no \':\'  statement'
        elif key == '':
            return 'There is no \':\' after the column or no key was entered'
        else:
            return q.QueryTop10(key, q.userInput[column], q.userInput[return_column])
    # crimes in column : key
    elif start == 'crimes':
        junk = read_until(string_list, 'in')
        column = read_until(string_list, ":").lower()
        key = read_until(string_list, '')
        if column not in q.userInput:
            return 'Column does not exist or there is no \'in\'  statement'
        elif key == '':
            return 'There is no \':\' after the column or no key was entered'
        else:
            return q.QueryNumCrimes(key, q.userInput[column])
    # return_column at column : key
    elif start in q.userInput:
        return_column = start.lower() + ' ' + read_until(string_list, 'at')
        column = read_until(string_list, ':').lower()
        key = read_until(string_list, '')
        if column not in q.userInput:
            return 'Column does not exist or there is no \':\'  statement'
        elif key == '':
            return 'There is no \':\' after the column or no key was entered'
        else:
            return q.QueryOne(key, q.userInput[column], q.userInput[return_column])
    # refresh
    elif start == 'refresh':
        return dbCreate.connect_database()
    elif start == 'exit':
        return 'Exiting...'
    elif start == 'help':
        return 'HELP STUFF HERE PLEASE WRITE ME'
    else:
        return 'Invalid query. Must start with \'top\', \'crimes\', or a column name.' \
               '\n You can also enter \'exit\', \'refresh\', or \'help\''


#dbCreate.connect_database()
read = ''
while read != 'exit':
    read = input('> ')
    print('\n' + parse_query(read) + '\n')
