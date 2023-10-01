#Web Scraping and Basic Data Analysis on COVID Data using Python
#A basic project in Python and Jupyter Notebook, to scrape and analyse some Coronavirus-related data.
#app.py is the Python source code for scraping data from worldometers.info. It uses BeautifulSoup library to parse the data from the website. The resultant data is stored in csv format with the file name corona.csv.

#Basic data analysis is done on the corona.csv file using Jupyter Notebook.(ass_1.ipynb).
#The data is checked, and duplicate and unnecessary rows are removed. Column data types are changed to more suitable formats. Graphical representation of the data is demonstrated.



import csv
import requests
from bs4 import BeautifulSoup

#scraping data from the website

html = requests.get('https://www.worldometers.info/coronavirus/').text
html_soup = BeautifulSoup(html, 'html.parser')
rows = html_soup.find_all('tr')


#function to extract text

def extract_text(row, tag):
    element = BeautifulSoup(row, 'html.parser').find_all(tag)
    text = [col.get_text() for col in element]
    return text

heading = rows.pop(0)

#extracting columns 1- 8

heading_row = extract_text(str(heading), 'th')[1:9]

#function to store the scraped data into a .csv file

def test():
    with open('corona.csv', 'w') as store:
        Store = csv.writer(store, delimiter=',')
        Store.writerow(heading_row)
        for row in rows:
            test_data = extract_text(str(row), 'td')[1:9]
            Store.writerow(test_data)

test()