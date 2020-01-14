
import pandas as pd
#pandas is a library required to analyse dataframes in python

import numpy as np

import matplotlib.pyplot as plt 
#matplotlib is required to generate graphs

import sys

try:
    data = pd.read_csv('items_for_antibacterial_drugs_per_1000_patients_on_list.csv', delimiter=',', header = 0 ,  na_values = ['0', '.'])
except IOError:
    print('Error: CSV file not found, please ensure you have downloaded the "items_for_antibacterial_drugs_per_1000_patients_on_list.csv" from the github repo and it is in the same folder as the python script')
    sys.exit(1) #Error handling ensures the CSV file containing the data has been downloaded. Prompts users if it cannot be found and terminates the script.

print(data)
#Reads in the csv with prescription data,
#header ensures first row in csv file becomes dataframe headers,
#na_values: all 0s converted to NaN

null_values = pd.notnull(data['total_list_size'])
#defines the variable 'null_values' as the NaN values in the column total_list_size

def reporting_null_values(df): #defining function to count where the total list size reported by the GP in that entry was 0, to feedback to the user
    
    removed_entries_list = 0 #Counter for below loop
    for bools in null_values:
        if bools == False: 
            removed_entries_list = removed_entries_list + 1
            #Count of entries(rows) that total_list_size is NaN, adds 1 to the removed_entries_list each time a NaN value is found. 


    print(removed_entries_list , 'entries were deleted as the GP had not specified their patient population on the entry. Other completed entries from the same GPs may still exist in the dataset')
    #Prints number of entries removed so user aware 

reporting_null_values(data) #Using above defined function on the dataframe called 'data'

final_data = data[null_values] #Creates a new dataframe called 'final_data' with all the rows which have NaN in the total_list_size column removed

pd.options.mode.chained_assignment = None #The below code is flagging the 'SettingWithCopy' warning, to warn that the
#operation may be being carried out on a copy. As the output is going into a new column, this is not an issue here.
#Results have been mannually checked and they are as expected. This code turns off the warning

final_data['items_per_1000'] = final_data['y_items'] / final_data['total_list_size'] * (1000)
#Creates a new column which calculates the items_per_1000 patients 


final_data['date'] = pd.to_datetime(final_data['date'], format='%Y-%m-%d') 
#Changes date column into datetime format recognised by python
pd.options.mode.chained_assignment = None #warning disabled as above


line_graph = final_data.groupby(pd.Grouper(key= 'date', freq='Y')).mean()['items_per_1000'].plot(legend=True) 
#grouby groups items from the dataframe as specified. 
#Grouper seperates the date column and groups everything just by year.
#.mean then finds the mean of each found line and the output of the plot is the items_per_thousand column of the dataframe.

#The below code generates a line graph of the mean number of prescriptions per 1000 patients across all GP practices for each year.
axes_line = plt.gca() #gca = get current access
axes_line.set_ylim([40,60]) #setting value parameters for the Y access
axes_line.set_ylabel('Mean items per 1000 patients') #Labelling Y and X access and creating a title
axes_line.set_xlabel('Year')
axes_line.set_title('Mean antibiotic pescriptions per 1000 patients')
plt.savefig('prescriptions_all_gps_linegraph.png', bbox_inches='tight') 
#saves the linegraph as a png file. 'tight' = removes white border

print('Line graph output has been saved to folder')
#informs the user that the line graph can be found in the folder

axes_boxplot = final_data[['items_per_1000', 'name']].boxplot(
                by='name', figsize=(20, 12), rot=90)
                #Creating a box plot from final_data dataframe
axes_boxplot.set_xlabel('') #Setting blank x label, labelling y axis and creating a title 
axes_boxplot.set_ylabel('Items per thousand patients')
axes_boxplot.set_title('Items per 1000 per practice')
plt.suptitle('')  # Getting rid of pandas-generated boxplot title
plt.savefig('prescriptions_per_gp_boxplot.png', bbox_inches='tight')
#saves the boxplot as a png file.

print('Box plot output has been saved to folder')
#informs the user that the boxplot can be found in the folder