import csv
import os
import string


def join_files_from(path: string) -> None:
    with open('lab_10/zad2.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile,delimiter=";")
        kolumny = ""
        for root, _, files in os.walk(path):
            # print(root)
            # print('    ', files)
            for file in files:
                with open(root+"/"+file , 'r') as f:
                    if kolumny == "":
                        kolumny = f.readline().removesuffix("\n").split(",")
                        writer.writerow(kolumny)
                    else:
                        f.readline()
                    for line in f:
                        writer.writerow(line.removesuffix("\n").split(","))
                        
        
join_files_from("lab_10/data_for_lab_10")