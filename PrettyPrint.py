import objects

class Out:

    def __init__(self):
        self._colours = objects.Colour()


    def __call__(self, msg, colour='white', bold=False, underline=False):
        colour = self._colours.cLookup[colour] if type(colour) == str else self._colours.cLookup['white'] # get the colour form the palate, default to white if input wrong
        if not bold or not underline:
            print(f"{colour}{msg}{self._colours.WHITE}")
        elif bold ^ underline:
            formatter = self._colours.BOLD if bold else self._colours.UNDERLINE
            print(f"{colour}{formatter}{msg}{self._colours.WHITE}")
        elif bold & underline:
            print(f"{colour}{self._colours.BOLD}{self._colours.UNDERLINE}{msg}{self._colours.WHITE}")