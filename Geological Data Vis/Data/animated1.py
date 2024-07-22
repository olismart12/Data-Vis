import pandas as pd
import json
import os
import webbrowser

# Read the CSV file
df = pd.read_csv('data/north_bowen_basin_geology.csv', header=0).convert_dtypes()

# Import the formats module
import formats
root = formats.getJson(df)

# Read the HTML template file
with open('animated/collapsible-tree.html', 'r') as file:
    content = file.read()

# Replace the placeholder with the JSON data
content = content.replace('"{{data}}"', json.dumps(root, indent=2))

# Write the updated content back to the HTML file
filename = os.path.abspath("animated/collapsible-tree.html")
with open(filename, 'w') as file:
    file.write(content)

# Open the HTML file in the web browser
webbrowser.open(filename)

