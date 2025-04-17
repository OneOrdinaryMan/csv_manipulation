import os
import pandas as pd
import re

#  Directory with your CSV files
input_dir = r"D:\Final Year Project\csv_manipulation\output1"

#  Extract year from column names like 'Mar-24', 'Dec-19'
def extract_year(col):
    match = re.search(r"-(\d{2})$", col.strip())
    if match:
        year = int(match.group(1))
        return 2000 + year if year < 50 else 1900 + year
    return 9999  # push non-year columns to end

#  Loop through CSV files
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_dir, filename)

        try:
            #  Read file with fallback encoding
            try:
                df = pd.read_csv(file_path, encoding="utf-8")
            except UnicodeDecodeError:
                df = pd.read_csv(file_path, encoding="ISO-8859-1")

            #  Separate first column (metric names)
            columns = df.columns.tolist()
            first_col = columns[0]
            year_cols = columns[1:]

            #  Sort year columns by extracted year only
            sorted_years = sorted(year_cols, key=lambda x: extract_year(x))
            new_order = [first_col] + sorted_years

            #  Reorder columns
            df_sorted = df[new_order]

            #  Save back to file
            df_sorted.to_csv(file_path, index=False, encoding="utf-8-sig")
            print(f" Reordered by year: {filename}")

        except Exception as e:
            print(f" Failed to process {filename}: {e}")
