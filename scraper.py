from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import csv
import requests

# Enter url of the wesite to be scraped
site = 'http://en.people.cn/'

def scrapeSite(url):
    start = datetime(2022, 1, 1)
    end = datetime(2022, 1, 10)
    keyword = 'the'
    
    # list to store the results
    keyWordList = []
    
    while start <= end:
        response = requests.get(url)        
        if response.status_code == 200:
            # parse and extract the text content of the response.
            # convert to lowercase and store the count of the keyword
            # increment the start date using timedelta(days=1)
            scrape = BeautifulSoup(response.text, 'html.parser')
            wordCount = scrape.get_text().lower().count(keyword)
            keyWordList.append({'Date': start.strftime('%Y-%m-%d'), 'Keyword': keyword, 'Count': wordCount})
        start += timedelta(days=1)

    # use csv.DictWriter to write rows to the CSV file.
    # use csvWriter.writeheader() to write the header row to the CSV file.
    # iterate through the list and write the data as rows in the CSV file.
    filename = 'keyword_count.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Keyword', 'Count']
        csvWriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
        
        csvWriter.writeheader()
        for x in keyWordList:
            csvWriter.writerow(x)

scrapeSite(site)
