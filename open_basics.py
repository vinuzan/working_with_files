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

