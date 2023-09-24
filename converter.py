import openai 
from utilities import get_prompt_for_mapping, get_prompt_for_conversion_functions
from dotenv import load_dotenv
from os import getenv 
import json 
import datetime 
import re 

load_dotenv()  
openai.api_key = getenv("OPENAI_API_KEY")

class Converter:
    def prompt(self, prompt):
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}], temperature=0.0)
        return chat_completion.choices[0].message.content

    def get_mapping(self, table, template):
        prompt = get_prompt_for_mapping(table, template)
        result = self.prompt(prompt)
        return json.loads(result)

    def get_conversion_functions_code(self, table, template, mapping):
        prompt = get_prompt_for_conversion_functions(table, template, mapping)
        result = self.prompt(prompt)
        return result 

