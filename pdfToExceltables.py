import pandas as pd
import pdfplumber
import xlsxwriter
import os

outputPath = "output"
path = "./input"

files = []
for filename in os.listdir(path):
    if filename.endswith(".pdf"):
        url = path + '/' + filename
        files.append(url)

# if file found
if files:
    print(files)
    prepared_list = []
    blank_row = []
    i = 0
    j = 0
    for file in files:
        with pdfplumber.open(file) as f:
            # looping with number of pages
            for page in f.pages:
                i+=1
                print("-- Working on page: ", i)
                for table in page.extract_tables():
                    j+=1
                    #prepared_list.append(blank_row)
                    #looping with number of tables
                    for row in table:
                        prepared_list.append(row)

    if j>=1:
        df = pd.DataFrame(prepared_list)
        if not os.path.exists(outputPath):
            os.makedirs(outputPath)

        writer = pd.ExcelWriter('./output/output.xlsx', engine='xlsxwriter')
        df.to_excel(writer,sheet_name='MergedTables', index=False,header=False)
        writer.close()
        print("Process completed")
    else:
        print("No tables found")
else:
    print("No PDF files selected")
