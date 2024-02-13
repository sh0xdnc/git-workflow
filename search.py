import pandas as pd

print('Enter search string')

uinput = input()

df = pd.read_excel('test.xlsx')

fdf = df[df['name'].str.contains(uinput)]

fdf.to_excel('output.xlsx', sheet_name='sheet1', index=False)