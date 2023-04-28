import streamlit as st
import pandas as pd
import numpy as np

import json

st.title('Test App')
st.write('Es funktioniert noch nicht wirklich, Irgendwie bricht er immer bei den Pandas Befehlen ab, kp warum.')

# Lade DataFrame
df2 = pd.read_json('data2.json')

# Zeig DataFrame in einer Tabelle an
st.table(df2)

# Zeig DataFrame im DataFrame-Viewer an
st.dataframe(df2)

# # def load_data(nrows):
# #     with open('data/data2.json', nrows=nrows) as d2:
# #         data2 = json.load(d2)
# #     return data2


# #data = load_data()
# #st.write(data)
# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# # Load 10,000 rows of data into the dataframe.
# data = load_data(100)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!')

# st.subheader('Raw data')
# st.write(data)
