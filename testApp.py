import streamlit as st
import pandas as pd
import numpy as np

import json

st.title('Test App')

#mit Pandas, geht noch nicht
# Read the JSON file into a Pandas dataframe
#df = pd.read_json('data/data2.json')

# Print the dataframe
# print(df)

#### normaler weg
# Open the JSON file and load its contents into a variable
with open('data/data2.json') as d2:
    data2 = json.load(d2)

# Print the contents of the JSON file
print(data2)
