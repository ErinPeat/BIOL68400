
import pandas as pd
#pandas is a library required to analyse dataframes in python

import numpy as np

import matplotlib.pyplot as plt 
#matplotlib is required to generate graphs

import sys

try:
    data = pd.read_csv('antibiotic_data.csv', 
        delimiter=',', header = 0 ,  na_values = ['0', '.'])
except IOError:
    print('Error: CSV file not found, please ensure you have downloaded the antibiotic_data.csv from the github repo titled filename and it is in the same folder as the python script')
    sys.exit(1) #Error handling ensures the CSV file containing the data has been downloaded. Prompts users if it cannot be found and terminates the script.

#Reads in the csv with prescription data,
#header ensures first row in csv file becomes dataframe headers,
#na_values: all 0s converted to NaN

def remove_null_values(df): #defining function to remove any null values from the dataframe

    null_values = pd.notnull(df['total_list_size'])
    #Labels entries with total list size 0 as False

    removed_entries_list = 0 #Counter for below loop
    for bools in null_values:
        if bools == False: 
            removed_entries_list = removed_entries_list + 1
            #Count of times total list size is 0/NaN

    final_data = df[null_values] #Removes all values that are labelled as NaN

    print(removed_entries_list , 'entries were deleted due to patient population not reported for this incidence, but GP data may exist in rest of the dataset')
    #Prints number of entries removed so user aware 

remove_null_values(data)

pd.options.mode.chained_assignment = None #The below code is flagging the 'SettingWithCopy' warning, to warn that the
#operation may be being carried out on a copy. As the output is going into a new column, this is not an issue here.
#Results have been mannually checked and they are as expected. This code turns off the warning

final_data['items_per_1000'] = final_data['y_items'] / final_data['total_list_size'] * (1000)
#Creates a new column which calculates the items_per_1000 patients 


final_data['date'] = pd.to_datetime(final_data['date'], format='%Y-%m-%d') 
#Changes date column into datetime format recognised by python
pd.options.mode.chained_assignment = None #warning disabled as above


#final_data.groupby([pd.Grouper(key= 'date', freq='Y'), 'name']).mean()
#final_data.groupby(pd.Grouper(key= 'date', freq='Y')).mean()


line_graph = final_data.groupby(pd.Grouper(key= 'date', freq='Y')).mean()['items_per_1000'].plot(legend=True) 
#grouby groups items from the dataframe as specified. 
#Grouper seperates the date column and groups everything just by year
#.mean then finds the mean of each found line and the output of the plot is the items_per_thousand column of the dataframe

axes_line = plt.gca() #gca = get current access
axes_line.set_ylim([40,60]) #setting value parameters for the Y access
axes_line.set_ylabel('Mean items per 1000 patients') #Labellong Y and X access and creating a title
axes_line.set_xlabel('Year')
axes_line.set_title('Mean antibiotic pescriptions per 1000 patients for all Manchester GPs 2015-2018')
plt.show()

print('Line graph output has been saved to folder')

axes_boxplot = final_data[['items_per_1000', 'name']].boxplot(
                by='name', figsize=(20, 12), rot=90)
                #Creating a box plot from dataframe from defined axis
axes_boxplot.set_xlabel(''); #Setting blank labels and naming others axis
axes_boxplot.set_ylabel('Items per thousand patients')
axes_boxplot.set_title('Items per 1000 per practice')
plt.suptitle('');  # Getting rid of pandas-generated boxplot title
plt.show() 
print('Box plot output has been saved to folder')