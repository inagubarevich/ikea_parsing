import requests
from bs4 import BeautifulSoup
import re
import csv


# вводим ссылку на страницу, которую будем парсить
url = 'https://www.ikea.com/ru/ru/catalog/categories/departments/living_room/10705/'

# получаем html-код
page = requests.get(url).text

def parsing(page):
    soup = BeautifulSoup(page, features="html.parser")

    # находим тег, в котором заключены данные по всем единицам товара
    product_block = soup.find('div', class_='productLists adproductLists')

    # находим теги, в каждом из которых заключена информация по каждому товару
    items = product_block.find_all('div', class_='productDetails ')

    # создаём список, в котором будем сохранять результаты
    global results
    results = []

    # далее извлекаем из нужных тегов информацию о каждом товаре
    k = 0

    for item in items:
        item_name = item.find('span', class_='productTitle floatLeft').text
        item_desc = item.find('span', class_='productDesp').text
        item_price = item.find('span', class_='price regularPrice').text

        # при помощи модуля re удаляем лишние пробелы из строки цены
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

# создаём функцию, которая будет создавать csv-файл и записывать в него данные
def save(results, path):
    with open('parsing.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Наименование', 'Описание', 'Цена', 'Ссылка'))

        writer.writerows(
            (result['Название'], result['Описание'], result['Цена'], result['Ссылка']) for result
            in results
        )

save(results, 'parsing.csv')

