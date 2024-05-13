import objects
import time

class Out:
    def __init__(self, log_name=None):
        if log_name is not None:
            filename = time.strftime("%Y%m%d-%H%M")+log_name+'.html'
            html_init_str = '<!DOCTYPE html>\n<html>\n  <head>\n        <title>'+filename+'</title>\n   </head>\n   <body>\n'
            self.log = open(filename, 'w')
            self.log.write(html_init_str)
        else:
            self.log = None

        self._colours = objects.Colour()

    def __call__(self, msg, colour='white', bold=False, underline=False, timestamp=False):
        colour_tag = self._colours.cLookup[colour] if type(colour) == str else self._colours.cLookup['white'] # get the colour form the palate, default to white if input wrong
        if timestamp:
            msg = time.strftime("%Y-%m-%d-%H:%M:%S - ")+msg
        if not bold or not underline:
            print(f"{colour_tag}{msg}{self._colours.WHITE}")
            if self.log is not None:
                self.log.write("""      <p style="color: {}; font-family: 'Liberation Sans',sans-serif">{}</p>\n""".format(colour, msg))
        elif bold ^ underline:
            formatter = self._colours.BOLD if bold else self._colours.UNDERLINE
            print(f"{colour_tag}{formatter}{msg}{self._colours.WHITE}")
            if self.log is not None:
                self.log.write("""      <p style="color: {}; font-family: 'Liberation Sans',sans-serif">{}</p>\n""".format(colour, msg))
        elif bold & underline:
            print(f"{colour_tag}{self._colours.BOLD}{self._colours.UNDERLINE}{msg}{self._colours.WHITE}")
            if self.log is not None:
                self.log.write("""      <p style="color: {}; font-family: 'Liberation Sans',sans-serif">{}</p>\n""".format(colour, msg))

    def __del__(self):
        html_closing_str = '    </body>\n</html>'
        if self.log is not None:
            self.log.write(html_closing_str)
            self.log.close()