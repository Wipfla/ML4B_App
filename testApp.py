import streamlit as st
import pandas as pd
import numpy as np

import json

st.title('ML4B_Libraries_Test App')
st.write('It works! :) Hallelujah!')

# Lade DataFrame
#df2 = pd.read_json('ML4B_App/data/data2/data2.json')
df_walk_Acc = pd.read_csv('data/NormalWalk/Accelerometer.csv')

# Zeig DataFrame in einer Tabelle an
#st.table(df_walk_Acc)

# Zeig DataFrame im DataFrame-Viewer an
st.dataframe(df_walk_Acc)

#Ballons
st.button('Click me!',on_click=st.balloons)

# Zeig DataFrame als Line Chart an
st.line_chart(data =df_walk_Acc)

#Frage
activity = st.radio(
    "What did he do?",
    ('Walk', 'PushUp', 'Jumping Jacks'))

match activity:
    case 'Walk':
        st.write('Correct! He walked.')

    case 'PushUp':
        st.write('You are incorrect.')
    
    case 'Jumping Jacks':
        st.write('You are incorrect.')