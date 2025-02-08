import pandas
import numpy



#read in data
data = pandas.read_csv('API_SP.DYN.LE00.IN_DS2_en_csv_v2_81.csv')
metadata = pandas.read_csv('Metadata_Country_API_SP.DYN.LE00.IN_DS2_en_csv_v2_81.csv')

#Remove regions from data
    #Step 1: Get the codes for regions. Note: regions will be missing a country code.
metadata = metadata[metadata['Region'].isna()]['Country Code'].tolist()
    #Step 2: remove the regions
data = data[~data['Country Code'].isin(metadata)]


#clean and export
data=data.transpose()
data.ffill() #TODO: Figure out why ffill is not working
data=data.transpose()
data.columns.str.lower().str.replace(' ','_')

data.to_csv('cleaned_data.csv', index=False, na_rep=0)

