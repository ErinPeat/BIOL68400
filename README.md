# BIOL68400

Hello and welcome to our repo! 

This code will has been written for the purposes of analysing prescription data by GP practice from the OpenPrescribing project. When run, this code will produce a line graph showing the mean number of prescriptions per year for the whole CCG and time period.

### Getting started

Before you can carry out any analysis, ensure you have the .csv downloaded which can be found in 'insert where we are going to put the file here!'
as this is the data required to carry out analysis using this code. 

After addtional packages have been imported, the script will attempt to load data from the filename.csv file and put it into a pandas dataframe

### Troubleshooting

* If the CSV upload does not occur correctly, the script will print: 

```
CSV file not found, please ensure you have downloaded the antibiotic_data.csv from the github repo titled filename and it is in the same folder as the python script.
```


* To ensure you can see both figures, one must be closed before the other can be opened. 

### Data source

Data is taken from the https://openprescribing.net/analyse/, which selected data as 

See prescribing data of 'drugs or BNF sections' & 'Antibacterial Drugs (5.1)'

versus 'total list size'

highlighting: 'a CCG or CCGs' 'CCG: NHS MANCHESTER CCG (14L)'

### Using a different dataset

To analyse data from a different CCG, please search for the dataset as described above, but replace 'CCG: NHS MANCHESTER CCG (14L)' with the CCG of your choice.

#### You MUST save the csv file as antibiotics_data.csv and in the same folder as the python script or the script will not run

Data reference: OpenPrescribing.net, EBM DataLab, University of Oxford, 2019

##### Created using Python 3. 
