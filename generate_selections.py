import json

# Read a CSV file and return a list of table names
def read_tables(file_name):
	table_names = []
	with open(f"./data/{file_name}.csv", "r") as tables_file:
		for row in tables_file:
			table_names.append(row.strip())

		print(table_names)
	
	return table_names

# Generate the DMS selection rules for the given table names
def generate_selection_rules(table_names, schema_name, rule_type):
	with open("./template/rules.json", "r") as template_file:
		
		data = json.load(template_file)

		index = 0
		for table in table_names:
			index += 1
			data["rules"].append(
				{
					"rule-type": rule_type,
					"rule-id": index,
					"rule-name": table+"_selector",
					"object-locator": {
						"schema-name": schema_name,
						"table-name": table
					},
					"rule-action": "include",
					"filters": []
				}
			)

		modified_data = json.dumps(data, indent=4)

		with open(f"./dms_mappings/{schema_name}_{rule_type}.json", "w") as modified_file:
			modified_file.write(modified_data)

# Invoke the functions
generate_selection_rules(read_tables("tables"), "production", "selection")