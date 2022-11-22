#Program for demonstrating Pandas library (Part B)

import pandas as pd
df = pd.read_excel('A05_sampleData.xlsx')

#display all data
print(df)

#display all rows with only 2 columns
df1 = pd.read_excel('A05_sampleData.xlsx', usecols=['Student_Name', 'Program'])
print(df1) 

#Filter data with numeric criteria: Display only students enrolled in more than 5 courses
df2=df.loc[df['Courses_Enrolled'] > 5] 
print(df2)
