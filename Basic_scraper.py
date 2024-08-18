from bs4 import BeautifulSoup as bfs
import requests
import csv

file = open('scraped.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Quote', 'Author'])

page = requests.get('http://quotes.toscrape.com')
soup = bfs(page.text, 'html.parser')
quotes = soup.findAll('span', attrs={'class':'text'})
authors = soup.findAll('small', attrs={'class':'author'})

for quote, author in zip(quotes, authors):
    print(quote.text + '-' + author.text)
    writer.writerow([quote.text, author.text])

file.close()
