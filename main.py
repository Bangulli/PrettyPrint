from PrettyPrint.figures import *
import time
import pandas as pd
import PrettyPrint as pp
from PrettyPrint import figures

df = pd.DataFrame({'Time': [1, 2], 'Place': [1, 2]})

fmt = pp.PPFormat([pp.ColourText('green')])
fmt1 = pp.PPFormat([pp.ColourText('red')])
printer = pp.Printer()

table = figures.Table(columns=df.columns, printer=printer, cell_num=[':.2f', ':.3f'], cell_fmt=fmt, frame_fmt=fmt1, col_width=10)

table.add_row([3, 3])