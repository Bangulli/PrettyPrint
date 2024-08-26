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
        self.effects = {
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

    def __call__(self):
        return

ansi_escape_sequences = {
    "default_text": "\033[39m",
    "black_text": "\033[30m",
    "red_text": "\033[31m",
    "green_text": "\033[32m",
    "yellow_text": "\033[33m",
    "blue_text": "\033[34m",
    "magenta_text": "\033[35m",
    "cyan_text": "\033[36m",
    "white_text": "\033[37m",
    "default_background": "\033[49m",
    "black_background": "\033[40m",
    "red_background": "\033[41m",
    "green_background": "\033[42m",
    "yellow_background": "\033[43m",
    "blue_background": "\033[44m",
    "magenta_background": "\033[45m",
    "cyan_background": "\033[46m",
    "white_background": "\033[47m",
    "bright_black_text": "\033[90m",
    "bright_red_text": "\033[91m",
    "bright_green_text": "\033[92m",
    "bright_yellow_text": "\033[93m",
    "bright_blue_text": "\033[94m",
    "bright_magenta_text": "\033[95m",
    "bright_cyan_text": "\033[96m",
    "bright_white_text": "\033[97m",
    "bright_black_background": "\033[100m",
    "bright_red_background": "\033[101m",
    "bright_green_background": "\033[102m",
    "bright_yellow_background": "\033[103m",
    "bright_blue_background": "\033[104m",
    "bright_magenta_background": "\033[105m",
    "bright_cyan_background": "\033[106m",
    "bright_white_background": "\033[107m",
    "rgb_text": rgb_text,
    "rgb_background": rgb_background
}