'''
Using this start file, use the dictionary to create a data frame with the produce names as rows and columns named - 
"Cost Per Pound", "Quantity Sold" and "Total Sale". NOTE: Please include the questions as part of your print statements so it is easier to grade.

Using Pandas Dataframe methods, display the following information:
'''

import pandas as pd
import numpy as np
from produce_dictionary import produce_dictionary

produce = pd.DataFrame(produce_dictionary,index=['Cost Per Pound','Quantity Sold','Total Sale'])
produce=produce.T

print(produce)


#Produce that had the highest and lowest sales in total sales (both name of produce and value)
#max_produce= (produce.iloc[[2]]).max()
max_produce_name= produce['Total Sale'].idxmax()
max_produce_value= produce['Total Sale'].max()
#max_produce= produce.max(axis=0)[['Total Sale']]
print(max_produce_name, max_produce_value)
#min_produce= (produce.min().iloc[[2]])
min_produce_name= produce['Total Sale'].idxmin()
min_produce_value= produce['Total Sale'].min()
#min_produce= produce.min(axis=0)[['Total Sale']]
print(min_produce_name, min_produce_value)


#Using 'loc', display the quantity and total sales for 'Orange' and 'Beets' (together)
oran_beets = produce.iloc[[35,33],[1,2]]
print(oran_beets)


#Using 'loc', display the total sales for 'Apples' through 'Lettuce'
apples_thru_lettuce = produce.iloc[20:29,[2]]
print(apples_thru_lettuce)


#Using 'at', update the quantity sold for Apricots to 11,955 and total sales to 44,353.05
print(produce['Quantity Sold'][11], produce['Total Sale'][11])
produce['Quantity Sold'][11] = 11955
produce['Total Sale'][11] = 44353.05
print(produce['Quantity Sold'][11], produce['Total Sale'][11])

#What is the average quantity sold across all products? (print out ONLY quantity sold)
avg_q_sold = produce.mean(axis=0)[['Quantity Sold']]
print(avg_q_sold)

#Create a new dataframe for only those produce that have sold between 11,500 to 12,000 (quantity)
produce2 = produce[produce["Quantity Sold"].between(11500,12000)]
#.between(11500,12000))
#pd.DataFrame
#[produce[produce[1]].between(11500,12000)]
print(produce2)


#What is the total sales for the products in the above new dataframe? (print out ONLY total sales)
prod2_total_sales = produce2.sum(axis=0)[[2]]
print(prod2_total_sales)







 