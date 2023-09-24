import unittest
import json
import pandas as pd 
import sys
sys.path.append('.')

from converter import Converter

class TestConverter(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def test_transferer(self):
        table = pd.read_csv('table_A.csv', nrows=10)
        template = pd.read_csv('template.csv', nrows=10)

        mapping = self.converter.get_mapping(table, template)
        mapping = {value: key for key, value in mapping.items()}

        result = self.converter.get_data_transfer(table, template, mapping)
        expected_result = {'Date': ['01-05-2023',
                                    '02-05-2023',
                                    '03-05-2023',
                                    '04-05-2023',
                                    '05-05-2023',
                                    '06-05-2023',
                                    '07-05-2023',
                                    '08-05-2023',
                                    '09-05-2023',
                                    '10-05-2023'],
                                    'EmployeeName': ['John Doe',
                                    'Jane Smith',
                                    'Michael Brown',
                                    'Alice Johnson',
                                    'Bob Wilson',
                                    'Carol Martinez',
                                    'David Anderson',
                                    'Eva Thomas',
                                    'Frank Jackson',
                                    'Grace White'],
                                    'Plan': ['Gold',
                                    'Silver',
                                    'Bronze',
                                    'Gold',
                                    'Silver',
                                    'Bronze',
                                    'Gold',
                                    'Silver',
                                    'Bronze',
                                    'Gold'],
                                    'PolicyNumber': ['AB12345',
                                    'CD67890',
                                    'EF10111',
                                    'GH12121',
                                    'IJ13131',
                                    'KL14141',
                                    'MN15151',
                                    'OP16161',
                                    'QR17171',
                                    'ST18181'],
                                    'Premium': [150, 100, 50, 150, 100, 50, 150, 100, 50, 150]}

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
