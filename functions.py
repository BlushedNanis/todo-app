FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Read the to-do items from the text file

    Args:
        filepath (_type_, optional): Filepath to the text file. Defaults to FILEPATH.

    Returns:
        _type_: List object with the to-do items, separated by '\n'
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos:list, filepath=FILEPATH):
    """Write the to-do items list object into the filepath.
    IMPORTANT: All the content in the file will be over written with the new lines.

    Args:
        todos (list): List of th to-do items
        filepath (_type_, optional): _Filepath to the text file. Defaults to FILEPATH.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos)
        

if __name__ == '__main__':
    # Get original todos content
    og_todos = get_todos()
    
    # Test the functions
    test = ["test 1\n", "test 2\n"]
    write_todos(test)
    test_result = get_todos()
    print(test_result)
    
    # Rewrite todos.txt back to the original content
    write_todos(og_todos)
    