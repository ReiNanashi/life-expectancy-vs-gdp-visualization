import pandas

input = pandas.read_csv('API_SP.DYN.LE00.IN_DS2_en_csv_v2_81.csv')
countries = pandas.read_csv('countries.csv')
#print(input.head())
#preFillInfo = input.info()

input.ffill()
input.columns.str.lower().str.replace(' ','_')
input.to_csv('cleaned_data.csv', index=False, na_rep=0)
input = input[input['Country Name'] in countries['country']]
print(input.info())
print(input.head())
