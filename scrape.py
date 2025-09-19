import requests
from bs4 import BeautifulSoup
import time
import csv
import send_mail
from datetime import date

urls = ["https://finance.yahoo.com/quote/AMZN/"," https://finance.yahoo.com/quote/GOOGL/", "https://finance.yahoo.com/quote/MSFT/"]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/140.0.0.0 Safari/537.36'
}

today =str(date.today()) + ".csv"
csv_file = open(today,"w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name', 'Current Price', 'Previous Close', 'Open', 'Bid', 'Ask', 'Day Range', '52 Week Range', 'Volume', 'Avg. Volume'])
                    

for url in urls:
    stock = []
    html_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_page.content, 'lxml')

    header_info = soup.find_all("div",id="svelte")[0]
    stock_content = header_info.find("main", class_="layoutContainer yf-9khyzo")
    stock_title = stock_content.find("h1").get_text()
    current_price = stock_content.find("div", class_="bottom yf-4vs57a").find("span").get_text()

    stock.append(stock_title)
    stock.append(current_price)
    table_info = stock_content.find_all("section", class_="gridLayout yf-9khyzo")[0].find_all("li")
    for i in range(0,8):
        value = table_info[i].find_all("span")[1].get_text()
        stock.append(value)
    
    csv_writer.writerow(stock)
    time.sleep(5)

csv_file.close()

send_mail.send(filename=today)
