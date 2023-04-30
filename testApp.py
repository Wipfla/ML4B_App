import streamlit as st
import pandas as pd
import numpy as np

import json

st.title('Test App')
st.write('Es funktioniert noch nicht wirklich, Irgendwie bricht er immer bei den Pandas Befehlen ab, kp warum.')

# Lade DataFrame
#df2 = pd.read_json('ML4B_App/data/data2/data2.json')
df2 = pd.read_csv('data/data2/Data2_Accelerometer_data.csv')
## Pierre: vielleicht ist der Path nicht richtig zur data2 und kann das deswegen nicht lesen/nicht im gleichen Directory wie der Code -> Error

# Zeig DataFrame in einer Tabelle an
#st.table(df2)

# Zeig DataFrame im DataFrame-Viewer an
st.dataframe(df2)
