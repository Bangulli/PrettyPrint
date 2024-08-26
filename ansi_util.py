COLOURS = {
    "default": 9,
    "black": 0,
    "red": 1,
    "green": 2,
    "yellow": 3,
    "blue": 4,
    "magenta": 5,
    "cyan": 6,
    "white": 7
}

EFFECTS = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "italic": "\033[3m",
    "underline": "\033[4m",
    "blink": "\033[5m",
    "inverse": "\033[7m",
    "hidden": "\033[8m",
    "strikethrough": "\033[9m"
}


class Text:
    def __init__(self, colour='default', option='default'):
        if isinstance(colour, str):
            if colour in COLOURS:
                if option == 'default':
                    self.fmt = f"\033[3{COLOURS[colour]}m"
                elif option == 'bright':
                    self.fmt = f"\033[9{COLOURS[colour]}m"
                else:
                    raise ValueError(f"Selected option doesnt exist, must be default or bright, got {option}")
            else:
                raise ValueError(f"Selected colour is not supported: {colour}")
        elif isinstance(colour, list) and all(isinstance(elem, int) for elem in colour) and isinstance(option, str):
            if option == 'default':
                self.fmt = f"\033[38;2;{colour[0]};{colour[1]};{colour[2]}m"
            elif option == 'bright':
                self.fmt = f"\033[98;2;{colour[0]};{colour[1]};{colour[2]}m"
            else:
                raise ValueError(f"Selected option doesnt exist, must be default or bright, got {option}")

            #self.fmt = f"\033[38;2;{colour[0]};{colour[1]};{colour[2]}m"
        else:
            raise TypeError('Passed colour is not a supported type! Supported types are string and list of int, got {} instead'.format(type(colour)))

    def __call__(self):
        return self.fmt


class Background:
    def __init__(self, colour='default', option='default'):
        if isinstance(colour, str):
            if colour in COLOURS:
                if option == 'default':
                    self.fmt = f"\033[4{COLOURS[colour]}m"
                elif option == 'bright':
                    self.fmt = f"\033[10{COLOURS[colour]}m"
                else:
                    raise ValueError(f"Selected option doesnt exist, must be default or bright, got {option}")
            else:
                raise ValueError(f"Selected colour is not supported: {colour}")
        elif isinstance(colour, list) and all(isinstance(elem, int) for elem in colour) and isinstance(option, str):
            if option == 'default':
                self.fmt = f"\033[48;2;{colour[0]};{colour[1]};{colour[2]}m"
            elif option == 'bright':
                self.fmt = f"\033[108;2;{colour[0]};{colour[1]};{colour[2]}m"
            else:
                raise ValueError(f"Selected option doesnt exist, must be default or bright, got {option}")

        else:
            raise TypeError(
                'Passed colour is not a supported type! Supported types are string and list of int, got {} instead'.format(
                    type(colour)))

    def __call__(self):
        return self.fmt

class Effect:
    def __init__(self, effect):
        self.effect = effect

    def __call__(self):
        return
