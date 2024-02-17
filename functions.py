FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    ''' Returns the to-do items in a list object from the filepath '''
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos, filepath=FILEPATH):
    ''' Write the to-do items list object into the filepath '''
    with open(filepath, 'w') as file:
        file.writelines(todos)
        

if __name__ == '__main__':
    print ("Hello, you are executing the functions module")