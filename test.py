import unittest
import ikea
import requests
from unittest.mock import MagicMock
import csv

page = requests.get('https://www.ikea.com/ru/ru/catalog/categories/departments/living_room/10705/').text

item = {'Название': 'ХЕМНЭС', 'Описание': 'консольный стол', 'Цена': '7999.–',
        'Ссылка': 'https://www.ikea.com/ru/ru/catalog/products/20388646/'}
# csv = MagicMock()
# csvfile.writer.assert_called_with(par)

class Test_Parser(unittest.TestCase):

    def test_parse(self):
        outcome = ikea.parsing(page)
        self.assertTrue(item in outcome)

    def test_html(self):
        k = type(page)
        self.assertTrue(k is str)

    def test_outcome(self):
        outcome = ikea.parsing(page)
        self.assertFalse(outcome is None)

    def test_list(self):
        outcome = ikea.parsing(page)
        self.assertTrue(type(outcome) is list)

    def test_read(self):
        csv_line = 'ХОЛ,стол-сундук,4999.–,https://www.ikea.com/ru/ru/catalog/products/20383154/'
        with open('parsing.csv') as csvfile:
            text = csv.reader(csvfile)
            self.assertTrue(csv_line in text)


if __name__ == '__main__':
    unittest.main()
