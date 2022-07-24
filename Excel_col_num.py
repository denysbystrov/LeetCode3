"""Number 171: Excel Column Sheet Number"""


def title_to_number(column_title: str) -> int:
    col_num = 0
    for i in range(len(column_title)):
        idx = len(column_title) - (i+1)
        col_num += (ord(column_title[idx]) - 64) * (26**i)

    return col_num

