from pathlib import Path, PureWindowsPath
import pandas as pd
import numpy as np

data_folder = Path.cwd() / "Dark Pool Data Feed/"
path_on_windows = PureWindowsPath(data_folder)
symbol = "HTHT"

excel_files = [file for file in data_folder.iterdir() if file.suffix == ".xlsx"]
result = []

for individual_excel_files in excel_files:
    data = pd.read_excel(individual_excel_files, header=0)
    data.columns = data.columns.str.strip()
    result.append(data)

result_concat = pd.concat(result)

filtered_results = result_concat[result_concat.Ticker == symbol]
filtered_results = filtered_results.iloc[:, :-9]
filtered_results.sort_values("Date", inplace=True)

filtered_results.to_excel(str(symbol) + " Results.xlsx", index=False)
print("Finished filtering data for " + str(symbol))