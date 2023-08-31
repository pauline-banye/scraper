import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def scrapeWeb(url):
    start = datetime(2022, 1, 1)
    end = datetime(2022, 2, 1)
    keyword = 'emissions'
    
    keyWordDict = {}
    
    while start <= end:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.get_text().lower()
            wordCount = content.count(keyword)
            keyWordDict[start.strftime('%Y-%m-%d')] = wordCount
        start += timedelta(days=1)
    
    csv_filename = 'carbon_word_count.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Date', 'No. of occurences'])  # Write the header row
        
        for date, wordCount in keyWordDict.items():
            csv_writer.writerow([date, wordCount])

website = 'http://en.people.cn/'
result = scrapeWeb(website)
for date, wordCount in result.items():
    print(f'Date: {date}, No. of times: {wordCount}')
    