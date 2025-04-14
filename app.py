import csv
from typing import List
def csv_list_parser(input_file_name: str)-> List[List[str]]:
    r_list=[]
    with open(input_file_name, newline='') as file:
        rows = csv.reader(file, delimiter=',')
        for row in rows:
            r_list.append(row)
    return r_list

def col_remover(input_list:List[List[str]])-> List[List[str]]:
    modified_list=[]
    for row in input_list:
        new_row=[]
        i=0
        while i < len(row):
            if row[i] == "":
                i +=2
                continue
            else:
                new_row.append(row[i])
                i+=1
        modified_list.append(new_row)
    return modified_list

def csv_writer(output_file_name, modified_list):
    with open(output_file_name, 'w+', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for line in modified_list:
            writer.writerow(line)
def main():
    input_file_name = "./data/ACC.csv"
    output_file_name = "./data/output/ACC.csv"
    input_list=csv_list_parser(input_file_name)
    modified_list=col_remover(input_list)
    csv_writer(output_file_name, modified_list)

if __name__ == "__main__":
    main()
