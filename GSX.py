from pathlib import Path, PureWindowsPath
import pandas as pd
import numpy as np

# Path for either OSX or Windows
data_folder = Path.cwd() / "Dark Pool Data Feed/"
path_on_windows = PureWindowsPath(data_folder)
symbol = "GSX"

# Iterate through directory to get all the Excel files
excel_files = [file for file in data_folder.iterdir() if file.suffix == ".xlsx" or file.suffix == ".xlsm"]
result = []

# Iterate through each individual Excel file and create a pandas dataform from it, clean up the column headers
for individual_excel_files in excel_files:
    data = pd.read_excel(individual_excel_files, header=0)
    data.columns = data.columns.str.strip()
    result.append(data)

# Concatenate each dataform into a single one
result_concat = pd.concat(result)

# Filter the results based on symbol specified above
filtered_results = result_concat[result_concat.Ticker == symbol]

# Strip out the last 9 columns that aren't needed
filtered_results = filtered_results.iloc[:, :-9]

# Sort the dataform by date column
filtered_results.sort_values("Date", inplace=True)

# Output to an Excel file
filtered_results.to_excel(str(symbol) + " Results.xlsx", index=False)

print("Finished filtering data for " + str(symbol))