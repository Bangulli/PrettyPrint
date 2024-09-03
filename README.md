# PrettyPrint - Yassify your console logs

This is the PrettyPrint package. It essentially wraps the ANSI escape sequences into an easy to use framework and provides some useful features for logging and status reporting in the console.<br>
This is my first ever package so be nice pls ; _ ;

## Contents

## Printing 
To use the ANSI printing features first import the package and create a Printer object.
Printer has two arguments:
- log_type: String, default None <br> Controls what type of log file will be created, see Logging
   
- timestamps: Bool, default False <br> False = no timestamps <br> True = Y-M-D-H:M:S timestamps each time printer gets called

To print something simply call the Printer object with your message as the argument
For employing different formats pass the fmt argument on call with your desired formatting configuration. See Formatting for more info.

    import PrettyPrint
    printer = PrettyPrint.Printer(log_type='txt', timestamps=True) # initialize printer object
    format = PrettyPrint.PPFormat() # initialize formatter object, more info on how to create a formatter in Formatting
    printer('hello world', fmt=format) # call printer to print

## Formatting
Ansi escape sequences are basically tags that control the text that follows afterward.
A great ressource to learn more about them is this Stackoverflow post, which is the main piece of information this package is built on: https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences

The main purpose of this package is to avoid having to build these sequences by hand. To do this you have three main options available:

- ColourText = The colour of the foreground text
- ColourBackground = The colour of the background
- Effect = Texteffects like bold, italic and underlined

### Options

- ColourText - controls the colour of the foreground text<br> Arguments:
  - colour: String or List
    - String: a valid colour from the list below
    - List: a list of RGB values as integers between 0 and 255
  - option: String
    - 'default': no change
    - 'bright': increases colour intensity


- ColourBackground - controls the colour of the background<br> Arguments:
  - colour: String or List
    - String: a valid colour from the list below
    - List: a list of RGB values as integers between 0 and 255
  - option: String
    - 'default': no change
    - 'bright': increases colour intensity
    

- Effect - controls the effects applied to the text <br> Arguments:
  - effect: String
    - a valid effect from the list below


- Colours: 
  - default
  - black
  - red
  - green
  - yellow
  - blue
  - magenta
  - cyan
  - white


- Effects:
  - reset: resets the format to default
  - bold: bold lettering
  - dim: decrease colour intensity
  - italic: italic lettering
  - underlined: underlines the text
  - inverted: switches background and text colour
  - strikethrough: letters appear as crossed out
  - double_underline: thick underlines
  - framed: encircles the text
  - encircled: same as above but with round corners
### PPFormat
Each of these options are objects that return an ANSI sequence on call, according to the specification on initialization.
You could technically use these objects by themselves and just get the sequence and append your message to it. In PrettyPrint however the PPFormat object is used to tie multiple options together and build a formatter to be passed to the Printer´s fmt argument.

PPFormat takes only one argument: options: list <br>
Options is a list of the formatting objects named above in no particular order.

    from PrettyPrint import *
    printer = Printer(log_type='txt', timestamps=True) # initialize printer object
    format = PPFormat([ColourText('black'), ColourBackground('white'), Effect('underlined')]) # initialize formatter object
    printer('hello world', fmt=format) # call printer to print


## Logging
Logfiles will be created with the name YMD-H:M_PrettyPrint_Autolog in the script working directory.
Logfiles are created when Printer is initialized with a valid log_type argument.
Valid log_types are:
- None = No file created
- 'txt' = Textfile, no colour support
- 'html' = Html file, colour support is work in progress

## Reporting
