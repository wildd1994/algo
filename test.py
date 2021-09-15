import main
from unittest import TestCase
import json


class TestJson(TestCase):

    def test_success(self):
        with open('config.json') as file:
            dict_tmp = json.load(file)
        self.assertEqual(main.check_cycle(dict_tmp), False)

    def test_unsuccess(self):
        with open('config1.json') as file:
            dict_tmp = json.load(file)
        self.assertEqual(main.check_cycle(dict_tmp), True)
