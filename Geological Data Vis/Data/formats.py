import pandas as pd

def getJson(df):
    nodes = {}
    root = {"name": "Basin Features", "children": []}
    
    for _, row in df.iterrows():
        feature = row['Feature']
        details = row['Details']
        
        if feature not in nodes:
            nodes[feature] = {"name": feature, "children": []}
            root["children"].append(nodes[feature])
        
        parent = nodes.get(feature)
        if parent is not None:
            parent["children"].append({"name": details})
    
    return root
