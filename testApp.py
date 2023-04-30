import streamlit as st
import pandas as pd
import numpy as np

import json

st.title('Test App')
st.write('It works! :) Hallelujah!')

# Lade DataFrame
#df2 = pd.read_json('ML4B_App/data/data2/data2.json')
df_walk_Acc = pd.read_csv('data/NormalWalk/Accelerometer.csv')

# Zeig DataFrame in einer Tabelle an
#st.table(df_walk_Acc)

# Zeig DataFrame im DataFrame-Viewer an
st.dataframe(df_walk_Acc)

# Zeig DataFrame als Bar Chart an
st.bar_chart(data =df_walk_Acc)