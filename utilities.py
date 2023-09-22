def get_table_text_description(table, table_name):
    table_dict = table.head(10).to_dict()
    description = f"""The table "{table_name}". It has following columns: """
    for key, value in table_dict.items():
        description += f"""column "{key}" with values: {', '.join(map(str, value.values()))}; """
    
    return description


def get_prompt_for_mapping(table, template, table_name, template_name):
    table_description = get_table_text_description(table, table_name)
    template_description = get_table_text_description(template, template_name)
    
    return f"""You are given two tables "{table_name}" and "{template_name}" with following descriptions:\n{table_description}\n{template_description}\nYou need to match similar columns. In case of ambiguous mapping, choose the first option. Don't return any code. Return a mapping with folowing format: {{"column_name_in_template": "column_name_in_table"}}"""