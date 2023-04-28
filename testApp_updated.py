import streamlit as st
import pandas as pd
import json

st.title('Test App')
st.write('Es funktioniert noch nicht wirklich, Irgendwie bricht er immer bei den Pandas Befehlen ab, kp warum.')

# Load DataFrame
df2 = pd.read_json('data2.json')

# Show DataFrame in a table
st.table(df2)

# Show DataFrame in the DataFrame Viewer
st.dataframe(df2)

def load_data(nrows):
    # Load data from JSON file
    with open('data2.json') as f:
        data = json.load(f)
    # Convert JSON data to DataFrame
    df = pd.DataFrame(data)
    # Return the first n rows of the DataFrame
    return df.head(nrows)

# Load and show the first 100 rows of data
data_load_state = st.text('Loading data...')
data = load_data(100)
data_load_state.text('Loading data...done!')

# Show the raw data in a subheader
st.subheader('Raw data')
st.write(data)