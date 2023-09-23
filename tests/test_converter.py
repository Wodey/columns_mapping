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
        
    def test_transferer(self):
        table = pd.read_csv('table_A.csv', nrows=10)
        template = pd.read_csv('template.csv', nrows=10)

        mapping = self.converter.get_mapping(table, template, "table", "template")
        mapping = {value: key for key, value in mapping.items()}

        result = self.converter.get_data_transfer(table, template, "table", "template", mapping)
        expected_result = {'Date': '05-01-2023, 05-02-2023, 05-03-2023, 05-04-2023, 05-05-2023, 05-06-2023, 05-07-2023, 05-08-2023, 05-09-2023, 05-10-2023',
                            'EmployeeName': 'John Doe, Jane Smith, Michael Brown, Alice Johnson, Bob Wilson, Carol Martinez, David Anderson, Eva Thomas, Frank Jackson, Grace White',
                            'Plan': 'Gold Plan, Silver Plan, Bronze Plan, Gold Plan, Silver Plan, Bronze Plan, Gold Plan, Silver Plan, Bronze Plan, Gold Plan',
                            'PolicyNumber': 'AB-12345, CD-67890, EF-10111, GH-12121, IJ-13131, KL-14141, MN-15151, OP-16161, QR-17171, ST-18181',
                            'Premium': '150.0, 100.0, 50.0, 150.0, 100.0, 50.0, 150.0, 100.0, 50.0, 150.0'
                            }

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
