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

def get_prompt_for_data_transfer(table, template, mapping):
    table_description = get_table_text_description(table, "table")
    template_description = get_table_text_description(template, "template")
    
    return f"""You are given the table and the template with following descriptions:\n{table_description}\n{template_description}\nYou should take every value from the table and convert it to the format of the template according to the mapping: {mapping}. Return json object. Be consistent with the format of the template"""


def get_prompt_for_data_transfer_fewshot(table, template, fewshot, new_table):
    table_description = get_table_text_description(table, "table")
    template_description = get_table_text_description(template, "template")
    fewshot_description = get_table_text_description(fewshot, "output")
    new_table_description = get_table_text_description(new_table, "table")
    
    return f"""{table_description}\n{template_description}\n{fewshot_description}\n{new_table_description}\n{template_description}\nThe output has following columns:"""

def parse_text_output(output):
    res = {}
    output = output.split('column')
    for row in output:
        if not row:
            continue 
        
        column = row.partition('with values:')[0].strip()

        res[column.replace('"', '')] = row.partition('with values:')[2].strip().split(';')[0].split(', ')
    return res 