import pandas as pd
import pdfplumber
import xlswriter
import os

outputPath = "output"
path = "./input"

files = []
for filename in os.listdir(path):
    if filename.endswith(".pdf"):
        url = path + '/' + filename
        files.append(url)

if files:
    print(files)
    prepared_list = []
    blank_row = []
    i = 0
    for file in files:
        with pdfplumber.open(file) as f:
            for page in f.pages:
                i+=1
                print("-- Working on page: ", i)
                for table in page.extract_tables():
                    #prepared_list.append(blank_row)
                    for row in table:
                        prepared_list.append(row)

    if i>=1:
        df = pd.DataFrame()
else:
    print("No PDF files selected")
