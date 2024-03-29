import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "http://library.ddn.upes.ac.in:8081/upeslib/questionbank/soc/btech_AI.html"

# For getting the HTMl
r = requests.get(url)
htmlContent = r.content
# HTML parser
soup = BeautifulSoup(htmlContent, 'html.parser')

list2=[]

for link in soup.find_all('a'):
    list2.append(link.get('href'))

del list2[0:9]
del list2[0]

fields= ['LINKS']
with open('CSV File.csv', 'w+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields)
    csv_writer.writerow(list2)


df = pd.DataFrame(list2, columns=['Links'])
df.to_csv('CSV File.csv')


