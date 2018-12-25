import unittest2
import ikea
import requests
import csv

page = requests.get('https://www.ikea.com/ru/ru/catalog/categories/departments/living_room/10705/').text

item = {'Название': 'ХЕМНЭС', 'Описание': 'консольный стол', 'Цена': '7999.–',
        'Ссылка': 'https://www.ikea.com/ru/ru/catalog/products/20388646/'}

class Test_Parser(unittest2.TestCase):

# checks if the part of the list is in the outcome of the function
    def test_parse(self):
        outcome = ikea.parsing(page)
        self.assertTrue(item in outcome)

# checks if the 7rd line is on it's place (checks the right order)
    def test_order(self):
        outcome = ikea.parsing(page)
        self.assertTrue(outcome[6] == item)

# checks if it gives the right string for first element after first function's execution
    def test_place_in_list(self):
        outcome = ikea.parsing(page)
        self.assertTrue(outcome[0]['Название'] == 'КЛИНГСБУ')

# checks if the csv-file is empty
    def test_read(self):
        with open('parsing.csv') as csvfile:
            text = [row for row in csv.DictReader(csvfile)]
            self.assertTrue(len(text) != 0)

# checks if the request module transforms page into html
    def test_html(self):
        k = type(page)
        self.assertTrue(k is str)

# checks if the outcome of parsing function is empty
    def test_outcome(self):
        outcome = ikea.parsing(page)
        self.assertFalse(outcome is None)

# checks if the result of function is list
    def test_list(self):
        outcome = ikea.parsing(page)
        self.assertTrue(type(outcome) is list)



if __name__ == '__main__':
    unittest2.main()
