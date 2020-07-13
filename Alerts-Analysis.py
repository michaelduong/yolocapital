from pathlib import Path, PureWindowsPath
import pandas as pd
import numpy as np

# Path for either OXS or Windows
data_folder = Path.cwd() / "Options Alerts Dump" / "Options Alerts"
path_on_windows = PureWindowsPath(data_folder)

# Iterate through directory to get all the Excel files
excel_files = [file for file in data_folder.iterdir() if file.suffix == ".csv"]
result = []

# Iterate through each individual Excel workbook, create a dataform, append to result array
for individual_files in excel_files:
    data = pd.read_csv(individual_files)
    result.append(data)

# Concatenate each dataform into one dataform
new_df = pd.concat(result)

# Drop irrelevant columns
new_df = new_df.iloc[:, 0:10]
new_df.drop(["SYMBOL", "TIME", "EXP", "STRIKE"], axis=1, inplace=True)

# Group data together based on DETAILS columns
grouped_df = new_df.groupby("DETAILS").agg({"%GAIN":['count', 'max', 'mean']})

# Output to Excel file
grouped_df.to_excel("BB Alert Result Statistics.xlsx")

print("Finished filtering statistics data for alerts")