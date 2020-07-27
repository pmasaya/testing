from bs4 import BeautifulSoup
import requests
import csv 

# returns HTML of website
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
#print(article.prettify())

headline = article.h2.a.text
#print(headline)

summary = article.find('div', class_='entry-content').p.text
print(summary)

#importing all articles

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

# open a csv file ('w' = write to this file)
csv_file = open('practice_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headlines', 'summary'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    print()

    csv_writer.writerow([headline, summary])

#close csv file
csv_file.close()

