import streamlit as st
import pandas as pd
import numpy as np

import json

st.title('Find the right Playlist for your Activity!')
st.info('Alexander Frey(), Pierre Engel(), Tawfik Madarati(), Marvin Wipfler (22959307)')
st.write('Just upload your data and we will find the right playlist for you!')

UserFile = st.file_uploader("Upload your File here and be amazed!", type={"csv", "txt", "json"})
if UserFile is not None:
    UserFile_df = pd.read_csv(UserFile)
    # Zeig DataFrame im DataFrame-Viewer an
    st.dataframe(UserFile_df)

    # Zeig DataFrame als Line Chart an
    st.caption('Your Data in Lines! WOW!')
    st.line_chart(data =UserFile_df, x='time', y=['x','y','z'])





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
st.caption('Gyroscope Data')
st.line_chart(data =df_JJ_Gyr, x='time', y=['x','y','z'])

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
