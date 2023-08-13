# AWS DMS MAPPING GENERATOR

Generate mapping rules for DMS tasks. This script aims to simplify creating the mapping rules in DMS.

1. Generate Selection Rules
Create a list of mapping rules selecting or excluding the given set of tables in a schema.

2. Generate Transformation Rules
Create a list of mapping rules for given list of columns in a table.

## Inputs Format (CSV File)

The inputs are a CSV file containing either the tables names or table name and columns for transformations

**Selection Rules**
Example - tables.csv

```html
<table_name>
<table_name>
<table_name>
```

**Transformation Rules**
Example - transformations.csv

```html
<table_name>,<column_name>,<column_name>,<column_name>
<table_name>,<column_name>,<column_name>,<column_name>,<column_name>
<table_name>,<column_name>,<column_name>
```

## Output Format (JSON)

**Selection Rules**
Example - production_selection

```json
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": 1,
            "rule-name": "table1_selector",
            "object-locator": {
                "schema-name": "production",
                "table-name": "table1"
            },
            "rule-action": "include",
            "filters": []
        }
    ]
}
```

**Transformation Rules**
Example - production_include-column

```json
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": 1,
            "rule-name": "table1_selector",
            "object-locator": {
                "schema-name": "production",
                "table-name": "table1"
            },
            "rule-action": "include",
            "filters": []
        },
        {
            "rule-type": "transformation",
            "rule-id": "11",
            "rule-name": "table1_column1_transformation",
            "rule-target": "column",
            "object-locator": {
                "schema-name": "production",
                "table-name": "table1",
                "column-name": "column1"
            },
            "rule-action": "include-column",
            "value": "null",
            "old-value": "null"
        }
    ]
}
```
