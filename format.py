class FormatKeys:
    def __init__(self):
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
        self.RESET = '\033[0m'

        self.fmtLookup = {
            'yellow':'\033[93m',
            'green':'\033[92m',
            'blue':'\033[94m',
            'cyan':'\033[96m',
            'red':'\033[91m',
            'white':'',
            'reset':self.RESET,
            'underline':self.UNDERLINE,
            'bold':self.BOLD
        }

    def fmt_query(self, requests):
        '''
        Takes a list of format requests and returns a concatenation of the requested items to parse in fromatting
        :param requests: list of fmtLookup keys
        :return:
        '''
        if type(requests) == list:
            fmt_string = ''
            for elem in requests:
                if self.fmt_key_exists(elem):
                    fmt_string += self.fmtLookup[elem]
                else:
                    raise TypeError('This format lookup key doesnt exist: {}'.format(elem))
            return fmt_string

    def fmt_key_exists(self, key):
        '''
        Checks if the key exists in the fmtLookup dictionary
        :param key: the key to check, string
        :return:
        '''
        return key in self.fmtLookup
