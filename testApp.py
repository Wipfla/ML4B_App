import streamlit as st
import pandas as pd
import numpy as np

import json

st.title('ML4B_Libraries_Test App')
st.write('')
st.write('It works! :) Hallelujah!')

# Lade DataFrame
#df2 = pd.read_json('ML4B_App/data/data2/data2.json')
df_JJ_Gyr = pd.read_csv('data/JJ_rightHand/Gyroscope.csv')

# Zeig DataFrame in einer Tabelle an
#st.table(df_walk_Acc)

# Zeig DataFrame im DataFrame-Viewer an
st.dataframe(df_JJ_Gyr)

#Ballons
st.button('Click me!',on_click=st.balloons)

# Zeig DataFrame als Line Chart an
st.line_chart(data =df_JJ_Gyr)

#Frage
activity = st.radio(
    "What did he do?",
    ('PushUp', 'Walk', 'Jumping Jacks'))

if activity == 'Walk':
    st.write('You are incorrect.')
elif activity == 'PushUp':
    st.write('You are incorrect.')
elif activity == 'Jumping Jacks':
    st.write('Correct!')
