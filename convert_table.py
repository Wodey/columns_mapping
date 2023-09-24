import argparse
from converter import Converter
import pandas as pd 
from pandas.api.types import is_numeric_dtype


def main(source_file, template_file, target_file):
    converter = Converter()
    table = pd.read_csv(source_file, nrows=10)
    template = pd.read_csv(template_file, nrows=10)
    # numeric_columns = template.columns[template.apply(is_numeric_dtype)]

    
    mapping = converter.get_mapping(table, template)
    mapping = {value: key for key, value in mapping.items()}

    converted_values = converter.get_data_transfer(table, template, mapping)
    converted_values = pd.DataFrame(converted_values)
    # converted_values[numeric_columns] = converted_values[numeric_columns].astype(float)
    # converted_values = converted_values.astype(template.dtypes.to_dict())
    converted_values.to_csv(target_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a CSV file using a template")
    parser.add_argument("--source", type=str, required=True, help="Source CSV file")
    parser.add_argument("--template", type=str, required=True, help="Template CSV file")
    parser.add_argument("--target", type=str, required=True, help="Target CSV file")

    args = parser.parse_args()

    main(args.source, args.template, args.target)