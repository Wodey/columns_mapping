def get_table_text_description(table, name):
    table_dict = table.head(10).to_dict()
    description = f"""The {name} has following columns: """
    for key, value in table_dict.items():
        description += f"""column "{key}" with values: {', '.join(map(str, value.values()))}; """
    
    return description


def get_prompt_for_mapping(table, template):
    table_description = get_table_text_description(table, "table")
    template_description = get_table_text_description(template, "template")
    
    return f"""You are given the table and the template with following descriptions:\n{table_description}\n{template_description}\nYou need to match similar columns. In case of ambiguous mapping, choose the first option. Don't return any code. Return a mapping with folowing format: {{"column_name_in_template": "column_name_in_table"}}"""

def get_prompt_for_conversion_functions(table, template, mapping):
    table_description = get_table_text_description(table, "table")
    template_description = get_table_text_description(template, "template")

    return f"""Pretend you have IQ 120.
{table_description}\n{template_description}
Write down the conversion function for every column in the table that is in the mapping {mapping}.
The conversion function should take the value of the table's column and transform it to the format of the template's column.
You can use regular expression, datetime, string, and other python libraries.
Return the code with all conversion functions and a dictonary "conversion_functions" that looks like that {{"table_column_name": "conversion_function_name"}}. Code should contain only functions and "conversion_functions" dict. Don't add anything extra. Code should be fully executable"""

def get_conversion_function(conversion_functions_code):
    exec(conversion_functions_code, globals())
    def main_conversion_function(x):
        for key, value in conversion_functions.items():
            try:
                x[key] = eval(value)(x[key].strip())
            except:
                x[key] = eval(value)(x[key])
            
        return x 
    return main_conversion_function