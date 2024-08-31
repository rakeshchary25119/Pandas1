import pandas as pd

data = [['Geeks', 5],
        ['for', 3]
        ['Geeks', 5]]

df1 = pd.DataFrame(data, columns = ['name', 'size'])
print(df1)


record = [['Geeks for Geeks', 22],
        ['LeetCode', 23],
        ['HackerRank', 234],
        ['interviewBit', 55]]

columns = ["Platforms", 'id']
df2 = pd.DataFrame.from_records(record, columns = columns)
print(df2)

dictData = [['Rakesh', 'chary', 'Bangaroj', 26],
            ['Rajesh', 'chary', 'Bangaroj', 23],
            ['Venkatesh', 'chary', 'Guntoju', 24]]

columns = ['First name', 'Middle name', 'Last name', 'Age']

df3 = pd.DataFrame.from_dict(dict(zip(columns, zip(*dictData))))
print(df3)