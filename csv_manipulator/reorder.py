# MIT License
#
# Copyright (c) 2025 Srivathsan Sudarsanan, Divyatejas Venkatesh
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import pandas as pd
import re


def reorder():
    #  Directory with your CSV files
    input_dir = "./output/"

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
