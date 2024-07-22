import pandas as pd
import formats

def generate_chart_data():
    # Read the CSV file
    df = pd.read_csv('data/north_bowen_basin_geology.csv', header=0).convert_dtypes()
    
    # Generate JSON data
    root = formats.getJson(df)
    
    # Return JSON data
    return root

if __name__ == "__main__":
    chart_data = generate_chart_data()
    print(json.dumps(chart_data, indent=2))
