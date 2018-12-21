import requests
from bs4 import BeautifulSoup
import re
import csv


# here is the link which we are going to parse
url = 'https://www.ikea.com/ru/ru/catalog/categories/departments/living_room/10705/'

# get html-code
page = requests.get(url).text

# create the list where we're going to save the results of parsing
results = []

def parsing(page):
    soup = BeautifulSoup(page, features="html.parser")

    # find tag containing information about all items we're going to parse
    product_block = soup.find('div', class_='productLists adproductLists')

    # find tags each of which contains information about one item
    items = product_block.find_all('div', class_='productDetails ')

    # further we get text information placed between that tags

    for item in items:
        item_name = item.find('span', class_='productTitle floatLeft').text
        item_desc = item.find('span', class_='productDesp').text
        item_price = item.find('span', class_='price regularPrice').text

        # with the help of module re delete unwanted spaces from the price line
        item_price = re.sub('[А-я, \s]', '', item_price)

        link = item.find('a').get('href')
        item_link = 'https://www.ikea.com' + link

        results.append({
            'Название' : item_name,
            'Описание' : item_desc,
            'Цена' : item_price,
            'Ссылка' : item_link
         })
    for a in results:
        print (a)

    return results

parsing(page)

# define function which will create new csv-file and write data in it

def save(results, path):
    with open('parsing.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Наименование', 'Описание', 'Цена', 'Ссылка'))

        writer.writerows(
            (result['Название'], result['Описание'], result['Цена'], result['Ссылка']) for result
            in results
        )

save(results, 'parsing.csv')

