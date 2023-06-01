import csv
from datetime import datetime
import re
import pickle

#Zad1
numbers = re.compile(r'\d+')
numbers_w_3_d = re.compile(r'\d{3,}')
ip4s = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
word_w_fg = re.compile(r'[A-Z][a-z]+')
lines_w_4d = re.compile(r'.+\s.+\s.+\s.+\n')
urls = re.compile(r'[https://|http://].+[/]')
def find_regex(filename, regex):
    finds = []
    with open(f'lab_11/{filename}', newline='', encoding="utf8",errors="ignore") as f:
        for line in f:
            finds+= re.findall(regex, line)
    return finds
            
print(find_regex("strings.txt",numbers))
print(find_regex("strings.txt",numbers_w_3_d))
print(find_regex("strings.txt",ip4s))
print(find_regex("strings.txt",word_w_fg))
print(find_regex("strings.txt",lines_w_4d))
print(find_regex("strings.txt",urls))
