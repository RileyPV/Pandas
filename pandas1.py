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

e = grades.values

print(grades.describe())

hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

f = hardware.str.contains('a')

g = hardware.str.upper()

#convert a series object to a python list
hardware_list = hardware.to_list()

ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,10])

#assign to variables
ds1 == ds2

ds1 > ds2

ds1 < ds2

#convert a series of lists to one series

list_of_series = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']
])

list_of_series = list_of_series.apply(pd.Series).stack().reset_index(drop=True)

#sort a series

s = pd.Series(['100', '200', 'python', '300.12', '400'])

sorted_series = s.sort_values()

#s = pd.Series(['100', 200, 'python', 300.12, '400'])
#sorted_series = s.sort_values()

#adding to a series
s = s.append(pd.Series(['500', 'php'])).reset_index(drop=True)

#write a pandas program to calculate the frequency counts of each unique
#value of a given series
import random
list1 = [random.randrange(1,10) for i in range(0,100)]
s = pd.Series(list1)

result = s.value_counts()

print()