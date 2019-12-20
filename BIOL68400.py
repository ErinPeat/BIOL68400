{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "#pandas is a library required to analyse dataframes in python\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "import matplotlib.pyplot as plt \n",
    "#matplotlib is required to generate graphs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('antibiotics_data.csv',\n",
    "     delimiter=',', header = 0 ,  na_values = ['0', '.'])\n",
    "'''Reads in the csv with prescription data,\n",
    "header ensures first row in csv file becomes dataframe headers,\n",
    "na_values: all 0s converted to NaN'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print (data)\n",
    "#Check that data has read in correctly. \n",
    "#Look for number and title of columns\n",
    "'''need to put in error thing'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "null_values = pd.notnull(data['total_list_size''])\n",
    "#Labels entries with total list size 0 as False\n",
    "\n",
    "removed_entries_list = 0 #Counter for below loop\n",
    "for bools in null_values:\n",
    "    if bools == False: \n",
    "        removed_entries_list = removed_entries_list + 1\n",
    "         #Count of times total list size is 0/NaN\n",
    "\n",
    "final_data = data[null_values] #Removes all values that are labelled as NaN\n",
    "        \n",
    "print(removed_entries_list , 'entries were deleted due to patient population not reported for this incidence, but GP data may exist in rest of the dataset')\n",
    "#Prints number of entries removed so user aware"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "final_data['patients/1000'] = final_data['total_list_size'] / (1000)\n",
    "#Creates new column in dataframe with patients per thousand"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "final_data['items_per_1000'] = final_data['y_items']\n",
    "                        / final_data['patients/1000'] \n",
    "#y_items is number of antibiotics pescribed by each GP per month/year shown in date \n",
    "#Creates new column in dataframe with perscriptions per thousand patients"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "final_data['date'] = pd.to_datetime(new_data['date'],\n",
    "                                    format='%Y-%m-%d') \n",
    "#Changes date column into datetime format recognised by python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#final_data.groupby([pd.Grouper(key= 'date', freq='Y'), 'name']).mean()\n",
    "#final_data.groupby(pd.Grouper(key= 'date', freq='Y')).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "line_graph = final_data.groupby(pd.Grouper(key= 'date', freq='Y'))\n",
    "                        .mean()['items_per_1000'].plot(legend=True) \n",
    "'''grouby groups items from the dataframe as specified. \n",
    "#Grouper seperates the date column and groups everything just by year\n",
    "#.mean then finds the mean of each found line and the output of the plot is the items_per_thousand column of the dataframe'''\n",
    "\n",
    "axes_line = plt.gca() #gca = get current access\n",
    "axes_line.set_ylim([40,60]) #setting value parameters for the Y access\n",
    "axes_line.set_ylabel('Mean items per 1000 patients') #Labellong Y and X access and creating a title\n",
    "axes_line.set_xlabel('Year')\n",
    "axes_line.set_title('Mean antibiotic pescriptions per 1000 patients for all Manchester GPs 2015-2018')\n",
    "plt.show()\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "axes_boxplot = final_data[['items_per_1000', 'name']].boxplot(\n",
    "                by='name', figsize=(20, 12), rot=90);\n",
    "                #Creating a box plot from dataframe from defined axis\n",
    "axes_boxplot.set_xlabel(''); #Setting blank labels and naming others axis\n",
    "axes_boxplot.set_ylabel('Items per thousand patients');\n",
    "axes_boxplot.set_title('Items per 1000 per practice');\n",
    "plt.suptitle('');  # Getting rid of pandas-generated boxplot title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "2.7.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
