from tabulate import tabulate
from texttable import Texttable

import latextable

def showLatexTable(titles,data,precision,dtype=[]):

    rows = []

    #add rows
    rows.append(titles)
    for row in data:
        rows.append(row)
    table = Texttable()
    table.set_cols_align(["c"] * len(titles))
    table.set_deco(Texttable.HEADER | Texttable.VLINES)
    table.set_precision(precision)
    if(dtype!=[]): 
        table.set_cols_dtype(dtype) # automatic
    table.add_rows(rows)
    print(data)

    print('\nTexttable Table:')
    print(table.draw())

    print('\nTexttable Latex:')
    print(latextable.draw_latex(table, caption=""))
