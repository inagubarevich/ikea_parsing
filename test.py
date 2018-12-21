import unittest2
import ikea
import requests


class Test_Parser(unittest2.TestCase):

    def test_html(self):
        page = requests.get('https://www.ikea.com/ru/ru/catalog/categories/departments/living_room/10705/').text
        k = type(page)
        self.assertTrue(k is str)

    def test_outcome(self):
        outcome = ikea.parsing(requests.get('https://www.ikea.com/ru/ru/catalog/categories/departments/living_room/10705/').text)
        self.assertFalse(outcome is None)

    def test_list(self):
        outcome = ikea.parsing(requests.get('https://www.ikea.com/ru/ru/catalog/categories/departments/living_room/10705/').text)
        self.assertTrue(type(outcome) is list)


if __name__ == '__main__':
    unittest2.main()

