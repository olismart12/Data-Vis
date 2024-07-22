import pandas as pd

# Data for North Bowen Basin Regional Geology
data = {
    'Feature': [
        'Age', 'Area', 'Maximum thickness', 'Maximum depth to base', 'Tectonic setting', 'Key structures', 
        'Basin overlies', 'Basin underlies', 'Basins adjacent', 'Cenozoic basins', 'North Bowen Basin'
    ],
    'Details': [
        'Cisuralian (Asselian) (~299 Ma) to Middle Triassic (Ladinian) (~238 Ma)',
        '83,114 km2 of south-west Queensland',
        '>10,000 m',
        '0 to >10,000 m',
        'Extension (Cisuralian), thermal subsidence (Guadalupian) and foreland (Lopingian to Middle Triassic) phases',
        'Taroom Trough, Denison Trough, Springsure Shelf, Comet Ridge, Collinsville Shelf, Capella Block, Nebo Synclinorium',
        'Thomson Orogen, Drummond Basin, Anakie Province',
        'Duaringa Basin, Emerald Basin, Biloela Basin, Redbank Basin, Yaamba Basin, Woorabinda Basin, Exevale Formation',
        'Galilee Basin, Gunnedah Basin',
        'Cenozoic hydrogeological unit: 1,200 m; Fluvial to lacustrine, intraplate volcanism',
        'Clematis: Fluvial to fluviolacustrine; Blackwater–Rewan: Fluvial (north) to offshore marine (south); Upper Back Creek: Coastal deltaic to offshore marine; Collinsville: Deltaic (north) to marine shelf (south); Reids Dome: Back arc to north, fluviolacustrine to south'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('north_bowen_basin_geology.csv', index=False)