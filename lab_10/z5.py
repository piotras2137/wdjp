import csv
from datetime import datetime
import string


def z5(filename: string, indx:int, src_format: string, dst_format: string) -> None:
    with open('lab_10/zad2.csv', newline='', encoding="utf8",errors="ignore") as f:
        with open(f'lab_10/{filename}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile,delimiter=";")
            reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
            kolumny = next(reader, None)
            writer.writerow(kolumny)
            for wiersz in reader:
                data = datetime.strptime(wiersz[indx], src_format)
                wiersz[indx] = data.strftime(dst_format)
                writer.writerow(wiersz)

z5("zad5",2,"%Y%m%d","%Y-%m-%d")