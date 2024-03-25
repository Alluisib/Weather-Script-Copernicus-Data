#Copernicus Data
import xarray as xr
import pandas as pd
from os import walk


dir_path = r"C:\Users\Brian\Documents\GitHub\Weather data\Data"

res = []
for (dir_path, dir_names, file_names) in walk(dir_path):
    res.extend(file_names)
    # don't look inside any subdirectory
    break


#used to find out information on the various files and variables included
'''
variables = ["fg", "hu", "pp", "rr", "tg", "tn", "tx"]
i = 0
for files in res:
    data_path = dir_path + "\\" + files
    print(data_path)

    data = xr.open_dataset(data_path)
    print(data[variables[i]])
    i += 1
'''
#get the mean temp data converted to csv
#res[4] is mean temps ("tg")
data_path = dir_path + "\\" + res[4]
sourcedata=xr.open_dataset(data_path)



temp_data= sourcedata['tg']
temp_data = temp_data[20000:,163,271]

print(temp_data)
df = temp_data.to_dataframe()
df.to_csv("test.csv")

