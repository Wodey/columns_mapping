import argparse
from converter import Converter
import pandas as pd 
from pandas.api.types import is_numeric_dtype
import time


def main(source_file, template_file, target_file):
    converter = Converter()
    table = pd.read_csv(source_file, nrows=10)
    template = pd.read_csv(template_file, nrows=10)
    output = template.drop(template.index)
    
    mapping = converter.get_mapping(table, template)
    mapping = {value: key for key, value in mapping.items()}


    chunksize = 10
    fewshot = None 
    is_fewshot = False 

    with pd.read_csv(source_file, chunksize=chunksize) as reader:
        for chunk in reader:
            if not is_fewshot:
                converted_values = converter.get_data_transfer(chunk, template, mapping)
                fewshot = pd.DataFrame(converted_values)
                is_fewshot = True 
            else:
                converted_values = converter.get_data_transfer_few_shot(table, template, fewshot, chunk)
            converted_values = pd.DataFrame(converted_values)
            output = pd.concat([output, converted_values])
            time.sleep(20) # I use this to avoid open ai request per minute limit, however with paid plan it is not necessary

    output.to_csv(target_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a CSV file using a template")
    parser.add_argument("--source", type=str, required=True, help="Source CSV file")
    parser.add_argument("--template", type=str, required=True, help="Template CSV file")
    parser.add_argument("--target", type=str, required=True, help="Target CSV file")

    args = parser.parse_args()

    main(args.source, args.template, args.target)