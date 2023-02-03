import pandas as pd
from string import ascii_uppercase as alfabeto

todas_tablas = pd.read_html('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')

dict_tablas = {}

for division, i in zip(alfabeto, range(9, 65, 7)):
    df = todas_tablas[i] 
    df.rename(columns={df.columns[1]: 'Team'}, inplace=True)
    df.pop('Qualification')
    dict_tablas[f'Grupo {division}'] = df
    
print(dict_tablas['Grupo A'])

