def Compose(structure):
    if is_list_of_callables(structure):
        fmt = ''
        for element in structure:
            fmt += element()
        return fmt
    else:
        raise TypeError('The passed variable is not a list of callables.')

def is_list_of_callables(variable):
    if isinstance(variable, list) and all(callable(item) for item in variable):
        return True
    return False