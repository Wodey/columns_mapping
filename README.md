This script creates a mapping from various sources to an Excel spreadsheet. The solution is based on ChatGPT, so you need an OpenAI key. During development, the initial table_A.csv was extended with ChatGPT to test how the script works with unseen data.

## How to use the script?

1. Install the required packages: `$ pip install requirements.txt`
2. Create an `.env` file with "OPENAI_API_KEY = YOUR OPEN AI API TOKEN".
3. Run the conversion script: `$ convert_table.py --source <source CSV> --template <template CSV> --target <target CSV>`

## Edge Cases

- If there are no columns in the source data that are similar to the template columns, we can ask the model to return an empty mapping (json object).
- In some cases where the data cannot be converted, we can ask model to simply mark such values as "None".
- In cases with large amounts of data, it may be cheaper to run a local model than to pay for the Open AI API.
- The above solution should also be considered in the case of sensitive data.
- Acceleration can also be achieved by using distributed solutions instead of pandas (e.g., dask).
