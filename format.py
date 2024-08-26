class PPFormat:
    def __init__(self, options='default'):
        if options == 'default':
            self.format = ''
        else:
            self.compose(options)

    def compose(self, structure):
        if self._is_list_of_callables(structure):
            fmt = ''
            for element in structure:
                fmt += element()
            self.format = fmt
        else:
            self.format = ''
            raise TypeError('The passed variable is not a list of callables.')


    def _is_list_of_callables(self, variable):
        if isinstance(variable, list) and all(callable(item) for item in variable):
            return True
        return False

    def __str__(self):
        return self.format
