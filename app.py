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

# imports
import csv
import os
from typing import List
import chardet


# function definitions
def csv_list_parser(input_file_name: str) -> List[List[str]]:
    with open(input_file_name, "rb") as file:
        encode = chardet.detect(file.read())
    r_list = []
    with open(input_file_name, encoding=encode["encoding"], newline="") as file:
        rows = csv.reader(file, delimiter=",")
        for row in rows:
            r_list.append(row)
    return r_list


def col_remover(input_list: List[List[str]]) -> List[List[str]]:
    modified_list = []
    for row in input_list:
        new_row = []
        i = 0
        while i < len(row):
            if row[i] == "":
                i += 2
                continue
            else:
                new_row.append(row[i])
                i += 1
        modified_list.append(new_row)
    return modified_list


def csv_writer(output_file_name, modified_list):
    with open(output_file_name, "w+", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        for line in modified_list:
            writer.writerow(line)


# main
def main():
    data_dir = "./data/"
    output_data_dir = "./output/"
    os.makedirs(output_data_dir, exist_ok=True)
    input_file_name = os.listdir(data_dir)
    for file in input_file_name:
        input_list = csv_list_parser(data_dir + file)
        modified_list = col_remover(input_list)
        csv_writer(output_data_dir + file, modified_list)


if __name__ == "__main__":
    main()
