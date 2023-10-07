import csv

import requests
from bs4 import BeautifulSoup

url = "http://idealsoftwares.com.br/indices/dolar2023.html"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('div', id='tabB')

    if table:
        data = []
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')

            if len(cells) >= 3:
                day = cells[0].text.strip()
                buy_text = cells[1].text.strip()
                sell_text = cells[2].text.strip()

                try:
                    buy = round(float(buy_text.replace(',', '.')), 2)
                    sell = round(float(sell_text.replace(',', '.')), 2)
                except ValueError:
                    buy = 0.0
                    sell = 0.0

                data.append([day, buy, sell])

        with open('dolar_setembro.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Data', 'Buy', 'Sell'])
            csv_writer.writerows(data)
    else:
        print('Table not found')

else:
    print('Results not found')
