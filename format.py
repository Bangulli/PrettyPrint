class PPFormat:
    def __init__(self, options='default'):
        if options == 'default':
            self.format = ''
        else:
            self.compose(options)

    def compose(self, structure):
        '''
        Concatenates all the subsequences to make a big combined sequence for formatting
        :param structure: a list of callables with objects from ansi_util
        :return:
        '''
        if self._is_list_of_callables(structure):
            fmt = ''
            for element in structure:
                fmt += element()
            self.format = fmt
        else:
            self.format = ''
            raise TypeError('The passed variable is not a list of callables.')


    def _is_list_of_callables(self, variable):
        '''
        Checks if the passed argument is a list of callables
        :param variable: the argument to check
        :return:
        '''
        if isinstance(variable, list) and all(callable(item) for item in variable):
            return True
        return False

    def __str__(self):
        return self.format
