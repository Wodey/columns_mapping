import unittest
import json
import pandas as pd 
import sys
sys.path.append('.')

from converter import Converter

class TestConverter(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def test_mapping(self):
        table = pd.read_csv('table_A.csv', nrows=10)
        template = pd.read_csv('template.csv', nrows=10)

        result = self.converter.get_mapping(table, template, "table", "template")
        expected_result = {
            "Date": "Date_of_Policy",
            "EmployeeName": "FullName",
            "Plan": "Insurance_Plan",
            "PolicyNumber": "Policy_No",
            "Premium": "Monthly_Premium"
            }

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
