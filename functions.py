# from main import file_path

FILE_PATH = r"todos.txt"

def get_todos():
    """ Read a text file and return the list of to-do items. """
    with open(FILE_PATH, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg):
    """ Write the to-do items list in the text file. """
    with open(FILE_PATH, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print('simple test')