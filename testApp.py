import streamlit as st
import pandas as pd
import numpy as np

import json

st.title('Test App')
st.write('Es funktioniert noch nicht wirklich, Irgendwie bricht er immer bei den Pandas Befehlen ab, kp warum.')

st.bar_chart(data= 'data/data2.json')

#mit Pandas
# Read the JSON file into a Pandas dataframe
#df = pd.read_json('data/data2.json')

# Print the dataframe
#print(df)

def load_data(nrows):
     data = pd.read_json('data/data2.json', nrows=nrows)
     return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(100)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader('Raw data')
st.write(data)



#### alternativer weg
# Open the JSON file and load its contents into a variable
#with open('data/data2.json') as d2:
#    data2 = json.load(d2)

# Print the contents of the JSON file
#print(data2)
