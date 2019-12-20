# %%
import pandas as pd
#pandas is a library required to analyse dataframes in python

import numpy as np

import matplotlib.pyplot as plt 
#matplotlib is required to generate graphs

# %%
data = pd.read_csv('antibiotics_data.csv',
     delimiter=',', header = 0 ,  na_values = ['0', '.'])
'''Reads in the csv with prescription data,
header ensures first row in csv file becomes dataframe headers,
na_values: all 0s converted to NaN'''

# %%
print (data)
#Check that data has read in correctly. 
#Look for number and title of columns
'''need to put in error thing'''

# %%
null_values = pd.notnull(data['total_list_size'])
#Labels entries with total list size 0 as False

removed_entries_list = 0 #Counter for below loop
for bools in null_values:
    if bools == False: 
        removed_entries_list = removed_entries_list + 1
         #Count of times total list size is 0/NaN

final_data = data[null_values] #Removes all values that are labelled as NaN
        
print(removed_entries_list , 'entries were deleted due to patient population not reported for this incidence, but GP data may exist in rest of the dataset')
#Prints number of entries removed so user aware

# %%
final_data['patients/1000'] = final_data['total_list_size'] / (1000)
#Creates new column in dataframe with patients per thousand

# %%
final_data['items_per_1000'] = final_data['y_items']
                        / final_data['patients/1000'] 
#y_items is number of antibiotics pescribed by each GP per month/year shown in date 
#Creates new column in dataframe with perscriptions per thousand patients

# %%


# %%
final_data['date'] = pd.to_datetime(new_data['date'],
                                    format='%Y-%m-%d') 
#Changes date column into datetime format recognised by python

# %%


# %%
#final_data.groupby([pd.Grouper(key= 'date', freq='Y'), 'name']).mean()
#final_data.groupby(pd.Grouper(key= 'date', freq='Y')).mean()

# %%
line_graph = final_data.groupby(pd.Grouper(key= 'date', freq='Y'))
                        .mean()['items_per_1000'].plot(legend=True) 
'''grouby groups items from the dataframe as specified. 
#Grouper seperates the date column and groups everything just by year
#.mean then finds the mean of each found line and the output of the plot is the items_per_thousand column of the dataframe'''

axes_line = plt.gca() #gca = get current access
axes_line.set_ylim([40,60]) #setting value parameters for the Y access
axes_line.set_ylabel('Mean items per 1000 patients') #Labellong Y and X access and creating a title
axes_line.set_xlabel('Year')
axes_line.set_title('Mean antibiotic pescriptions per 1000 patients for all Manchester GPs 2015-2018')
plt.show()
%matplotlib inline

# %%
axes_boxplot = final_data[['items_per_1000', 'name']].boxplot(
                by='name', figsize=(20, 12), rot=90);
                #Creating a box plot from dataframe from defined axis
axes_boxplot.set_xlabel(''); #Setting blank labels and naming others axis
axes_boxplot.set_ylabel('Items per thousand patients');
axes_boxplot.set_title('Items per 1000 per practice');
plt.suptitle('');  # Getting rid of pandas-generated boxplot title

# %%


# %%
