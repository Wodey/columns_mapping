import argparse

def main(source_file, template_file, target_file):
    # Your code to convert the table goes here
    print(source_file, template_file, target_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a CSV file using a template")
    parser.add_argument("--source", type=str, required=True, help="Source CSV file")
    parser.add_argument("--template", type=str, required=True, help="Template CSV file")
    parser.add_argument("--target", type=str, required=True, help="Target CSV file")

    args = parser.parse_args()

    main(args.source, args.template, args.target)