import argparse
from converter import Converter
import pandas as pd 
from pandas.api.types import is_numeric_dtype
from utilities import get_conversion_function

def main(source_file, template_file, target_file):
    converter = Converter()
    table = pd.read_csv(source_file, nrows=10)
    template = pd.read_csv(template_file, nrows=10)
    output = template.drop(template.index)
    
    mapping = converter.get_mapping(table, template)
    mapping = {value: key for key, value in mapping.items()}

    conversion_functions_code = converter.get_conversion_functions_code(table, template, mapping)

    main_conversion_function = get_conversion_function(conversion_functions_code)

    full_table = pd.read_csv(source_file)
    full_table.columns = full_table.columns.str.strip()
    res = full_table[mapping.keys()].apply(main_conversion_function, axis=1)
    
    res.rename(columns=mapping, inplace=True)
    res = res.astype(template.dtypes.to_dict())


    res.to_csv(target_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a CSV file using a template")
    parser.add_argument("--source", type=str, required=True, help="Source CSV file")
    parser.add_argument("--template", type=str, required=True, help="Template CSV file")
    parser.add_argument("--target", type=str, required=True, help="Target CSV file")

    args = parser.parse_args()

    main(args.source, args.template, args.target)
    # main("table_A.csv", "template.csv", "result.csv")