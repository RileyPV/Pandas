'''
Using this start file, use the dictionary to create a data frame with the produce names as rows and columns named - 
"Cost Per Pound", "Quantity Sold" and "Total Sale". NOTE: Please include the questions as part of your print statements so it is easier to grade.

Using Pandas Dataframe methods, display the following information:
'''

import pandas as pd
import numpy as np
from produce_dictionary import produce_dictionary

produce = pd.DataFrame(produce_dictionary,index=['Cost Per Pound', 'Quantity Sold', 'Total Sale'])

print(produce)


#Produce that had the highest and lowest sales in total sales (both name of produce and value)
min_produce= ()
print(min_produce)
    #(produce.min(), produce_dictionary['Name'])
#max_produce= 
    #(produce.max(), produce_dictionary['Name'])


#Using 'loc', display the quantity and total sales for 'Orange' and 'Beets' (together)
oran_beets = produce.iloc[[1,2],[35,33]]
print(oran_beets)


#Using 'loc', display the total sales for 'Apples' through 'Lettuce'
apples_thru_lettuce = produce.iloc[[2][20:28]]
print(apples_thru_lettuce)


#Using 'at', update the quantity sold for Apricots to 11,955 and total sales to 44,353.05



#What is the average quantity sold across all products? (print out ONLY quantity sold)



#Create a new dataframe for only those produce that have sold between 11,500 to 12,000 (quantity)
produce2 = [produce['Quantity Sold'].between(11500,12000)]
print(produce2)


#What is the total sales for the products in the above new dataframe? (print out ONLY total sales)
prod2_total_sales = produce2[1].sum()
print(prod2_total_sales)







 