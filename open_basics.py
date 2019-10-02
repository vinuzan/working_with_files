#Here we define our open and closed functions

def open_read_file(file):

    try:
        opened_file = open(file, 'r')
        file_lines_list = opened_file.readlines()
        print(file_lines_list)

        for line in file_lines_list:
            print(line.rstrip('\n'))

        opened_file.close() #otherwise file is locked and cant be changed.

    except FileNotFoundError as error_msg:
        print('File cannot be found')
        raise
    except SyntaxError as errmsg:
        print('There has been a syntax error')
        raise


#Using With - same function as above but doesnt need close.
def open_read_file_using_with(file):

    try:
        with open(file, 'r') as open_file:
            for line in open_file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError as error_msg:
        print('File cannot be found')
        #raise - the red message
    finally:
        print('\n Execution completed')


#Writing format
def write_to_file(file, order_item):
    try:
        opened_file = open(file, 'a')
        opened_file.write(order_item)

        opened_file.close()
    except FileNotFoundError:
        print('File not found!')