#Program for learning pandas library

import pandas as pd
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
    'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
    'wins': [11, 8, 10, 15, 11, 6, 10, 4],
    'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
print("=== whole DateFrame ===")
print(football)
# list of columns to show
columns_to_show = ['team','wins']
print("=== all rows with only colums to show ===")
print(football[columns_to_show])
print("=== only first two rows ===")
print(football[columns_to_show].head(2))
print("=== all rows where wins are greate than or equal to 10 ===")
print(football[football.wins >= 10])
