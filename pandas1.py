import pandas as pd

grades = pd.Series([87,100,94], index=['Wally', 'Eva', 'Sam'])

#print(grades)

grades_dict = {'Wally' : 87, 'Eva' : 100, 'Sam' : 94}

grades_ds = pd.Series(grades_dict)

a = pd.Series(98.6, range(3))

print(grades_ds)

eva = grades['Eva']

print(eva)

wally = grades.Wally

print(wally)

b = grades[0]

c = grades.count()

d = grades.mean()


print(grades.describe())

print()