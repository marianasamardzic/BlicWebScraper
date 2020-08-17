from bs4 import BeautifulSoup
import requests
import csv

base = 'https://www.blic.rs/vesti'

csv_file = open('blic_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['header', 'text', 'datetime'])

for i in range(1,6):

    if i == 1 :
        source = requests.get(base).text
    else:    
        source = requests.get(f'{base}?strana={i}').text

    soup = BeautifulSoup(source, 'lxml')
    for article in soup.find_all('article'):
        #print(article)
        header = article.h3.text
        print(header)
        
        link = article.a['href']
        page = requests.get(link).text
        pageSoup = BeautifulSoup(page, 'lxml')
        articleBody = pageSoup.find('div', class_='article-body')
        time = pageSoup.time.text
        print(time.strip())
        text = ""
        for p in articleBody.find_all('p'):
            text+= p.text
        print(text)
        print()

        csv_writer.writerow([header, text, time])

csv_file.close()