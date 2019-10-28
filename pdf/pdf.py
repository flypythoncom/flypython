#!/usr/bin/env python3

import pdfplumber
import pandas as pd

with pdfplumber.open("test.pdf") as pdf:
    first_page = pdf.pages[0]
    text = first_page.extract_text()
    print(text)

    second_page = pdf.pages[1]
    table = second_page.extract_tables()
    for t in table:
        df = pd.DataFrame(t[1:],columns=t[0])
        print(df)

