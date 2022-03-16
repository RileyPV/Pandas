import pandas as pd

pd.set_option("precision" , 2)

grades_dict = {"Wally" : [87,96,70],
                "Eva" : [100,87,90],
                "Sam" : [94,77, 90],
                "Katie" : [100, 81, 82],
                "Bob" : [83,65,85],}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1', 'Test2', 'Test3']

print(grades)

eva = grades['Eva']

sam = grades.Sam

#using the loc and iloc methods
test2 = grades.loc['Test2']

test1 = grades.iloc[0]

#for consecutive rows
test1_thru_test3 = grades.loc['Test1':'Test3']
#for non-consecutive rows
test1_and_test3 = grades.loc[['Test1', 'Test3']]

test1_and_test2 = grades.iloc[0:2]

#view only Eva's and Katie's grades for Test1 and Test2
eva_katie_test1_test2 = grades.loc['Test1':'Test2',['Eva','Katie']]
print(eva_katie_test1_test2)

#view only Sam's THRU Bob's grades for Test1 and Test3
sam_thru_bob_test1_test3 = grades.loc[['Test1','Test3'], 'Sam':'Bob']
print(sam_thru_bob_test1_test3)

#Boolean Indexing
#select everyone with an A grade

grades_A = grades[grades>=90]

#create a dataframe for everyone with a B grade
grades_b = grades[(grades>= 80) & (grades <= 90)]

#create a dataframe for everyone with an A or B grade
grades_A_or_B = grades[(grades>=90) | (grades >= 80)]



#by student
print(grades.describe())

#by test
print(grades.T.describe())

#Exercise - Get the average of all the students grades on each test
print(grades.T.mean())

#sort rows by their indices (test name)
r_sorted_grades_i = grades.sort_index(ascending=False)

#sort columns by their column names (student names)
#axis = 1 indicates to sort by column indices
#axis = 0 indicates to sort by row indices

c_sorted_grades_i = grades.sort_index(axis=1)

#in reverse sort order
c_sorted_grades_i = grades.sort_index(axis=1,ascending=False)

print()