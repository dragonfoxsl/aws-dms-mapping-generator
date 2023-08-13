import json

# Read a CSV file and return a list of transformations
def read_transformations(file_name):
	table_transformations = []

	with open(f"./data/{file_name}.csv", "r") as transformations_file:
		for row in transformations_file:
			table_transformations.append(row.strip())

		print(table_transformations)
	
	return table_transformations

# Generate the DMS selection and transformation rules
def generate_selection_rules(table_transformations, schema_name, transform_action):
	with open("./template/rules.json", "r") as template_file:
		
		data = json.load(template_file)

		index = 0
		for transformation in table_transformations:
			index += 1

			transformation_data = []
			for column in transformation.split(","):
				transformation_data.append(column)

			table_name = ""
			for colindex, column in enumerate(transformation_data):
				if (colindex == 0):
					table_name = str(column).strip()
					data["rules"].append(
						{
							"rule-type": "selection",
							"rule-id": index,
							"rule-name": f"{column}_selector",
							"object-locator": {
								"schema-name": schema_name,
								"table-name": table_name
							},
							"rule-action": "include",
							"filters": []
						}
					)
				else:
					data["rules"].append(
						{
							"rule-type": "transformation",
							"rule-id": f"{index}{colindex}",
							"rule-name": f"{table_name}_{column}_transformation",
							"rule-target": "column",
							"object-locator": {
								"schema-name": schema_name,
								"table-name": table_name,
								"column-name": column
							},
							"rule-action": transform_action,
							"value": "null",
							"old-value": "null"
						}
					)

		modified_data = json.dumps(data, indent=4)

		with open(f"./dms_mappings/{schema_name}_{transform_action}.json", "w") as modified_file:
			modified_file.write(modified_data)

# Invoke the functions
generate_selection_rules(read_transformations("transformations"),"production", "include-column")