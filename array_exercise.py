## Numpy Exercise
import numpy as np 

## Step 1: Create a 4x3 array of all 2s
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
integers = np.full((4,3),2)
print(integers)

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
integers1 = np.arange(0,120,10).reshape(3,4)
print(integers1) 

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print("-----------------------------------------------   STEP THREE   -----------------------------------------------")
integers2 = integers1.reshape(4,3)
print(integers2)

## Step 4: Multiply every elemnt of the above array by 3 and store the new values in a different array
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
integers3 = integers2 * 3
print(integers3)

## Step 5: Multiply your array from step one by your array from step 2
print("-----------------------------------------------   STEP FIVE   -----------------------------------------------")
#integers4 = integers * integers1
## This errored out... why?
#The arrays were different dimensions. The Rows dont matter but the columns do.
#print(integers4)

## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print("-----------------------------------------------   STEP SIX   -----------------------------------------------")
integers5 = integers * integers2
## this worked! why?
#The Columns in the arrays are the same so it worked.
print(integers5)



