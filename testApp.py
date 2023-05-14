import streamlit as st
import pandas as pd
import numpy as np
import json

# Seite 1
def page1():
    st.subheader('Playlist Recommender')
    # Fügen Sie hier den Inhalt der Seite 1 hinzu
    
    st.title('Find the right Playlist for your Activity!')

    st.write('Just upload your data and we will find the right playlist for you!')

    UserFile = st.file_uploader("Upload your File here and be amazed!", type={"csv", "txt", "json"})
    if UserFile is not None:
        UserFile_df = pd.read_csv(UserFile)
        # Zeig DataFrame im DataFrame-Viewer an
        st.dataframe(UserFile_df)

        #Extract Gyr Data, Acc Data, Orientation Data if user file is a json file
        #if UserFile.name.endswith('.json'):
            #hier muss noch eine Funktion gebaut werden die die Daten aus dem json file extrahiert (siehe test.ipynb)
            #die einzelnen Tabellen müssen dann noch in die Datenbank geladen werden bzw. concateniert werden
    
        # Zeig DataFrame als Line Chart an
        st.caption('Your Gyroscope Data in Lines! WOW!')
        st.line_chart(data =UserFile, x='time', y=['x','y','z'])




    st.info('Alexander Frey(23169187), Pierre Engel(), Tawfik Madarati(), Marvin Wipfler (22959307)')  

# Seite 2
def page2():
    st.subheader('Test Page')
    # Fügen Sie hier den Inhalt der Seite 2 hinzu
    st.title('Test Page for messing around!')
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
        
# Seitenleiste
st.sidebar.title('Navigation')
pages = {
    'Seite 1': page1,
    'Seite 2': page2
}
selection = st.sidebar.radio("Gehe zu", list(pages.keys()))

# Seiteninhalt
page = pages[selection]
page()


