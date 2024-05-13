import objects
import time

class Out:
    def __init__(self, log_type=None, timestamps=False):
        '''
        Initialize the the Outputter. On call takes a text and prints it to console with the specified formatting
        Also logs everything to a file if log_type is {html, txt}
        :param log_type: the type of logfile created, if None, no file is created. if 'html' formatted html, if 'txt' plain text txt
        :param timestamps: controls whether to print timestamps before each output
        '''
        if log_type in ['html', 'txt']:
            self.log_type = log_type
            filename = time.strftime("%Y%m%d-%H%M")+'_PrettyPrint_Autolog'+'.'+self.log_type
            self.log = open(filename, 'w')
            if log_type == 'html':
                html_init_str = '<!DOCTYPE html>\n<html>\n  <head>\n        <title>'+filename+'</title>\n   </head>\n   <body>\n'
                self.log.write(html_init_str)
        else:
            self.log = None

        self._colours = objects.Colour()
        self.timestamps = timestamps

    def __call__(self, msg, colour='white', bold=False, underline=False):
        '''
        Prints a formatted message to the console and logs it to a file if log_type is {html, txt}
        :param msg: String The text to be printed
        :param colour: String The colour of the printout {red, blue, green, yellow, white, cyan}
        :param bold: Bool Controls if the message should be bold
        :param underline: Bool Controls if the message should be underlined
        :return:
        '''
        colour_tag = self._colours.cLookup[colour] if type(colour) == str else self._colours.cLookup['white'] # get the colour form the palate, default to white if input wrong
        if self.timestamps:
            msg = time.strftime("%Y-%m-%d-%H:%M:%S - ")+msg
        if not bold or not underline:
            print(f"{colour_tag}{msg}{self._colours.WHITE}")
            if self.log is not None:
                if self.log_type == 'html':
                    self.log.write("""      <p style="color: {}; font-family: 'Liberation Sans',sans-serif">{}</p>\n""".format(colour, msg))
                elif self.log_type == 'txt':
                    self.log.write(msg+'\n')
        elif bold ^ underline:
            formatter = self._colours.BOLD if bold else self._colours.UNDERLINE
            print(f"{colour_tag}{formatter}{msg}{self._colours.WHITE}")
            if self.log is not None:
                if self.log_type == 'html':
                    self.log.write("""      <p style="color: {}; font-family: 'Liberation Sans',sans-serif">{}</p>\n""".format(colour, msg))
                elif self.log_type == 'txt':
                    self.log.write(msg+'\n')
        elif bold & underline:
            print(f"{colour_tag}{self._colours.BOLD}{self._colours.UNDERLINE}{msg}{self._colours.WHITE}")
            if self.log is not None:
                if self.log_type == 'html':
                    self.log.write("""      <p style="color: {}; font-family: 'Liberation Sans',sans-serif">{}</p>\n""".format(colour, msg))
                elif self.log_type == 'txt':
                    self.log.write(msg+'\n')

    def __del__(self):
        '''
        Called on delete to close the file and finish html if log_type is html
        :return:
        '''
        if self.log is not None:
            if self.log_type == 'html':
                html_closing_str = '    </body>\n</html>'
                self.log.write(html_closing_str)
            self.log.close()