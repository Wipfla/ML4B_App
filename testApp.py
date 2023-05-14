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

    UserFile = st.file_uploader("Upload your File here and be amazed!", type={"csv", "json"})
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


    #Hier müssen wir noch den Algo einbauen für die Playlist und vlt einen Button der dich zur Playlist weiterleitet


    st.info('Alexander Frey(23169187), Pierre Engel(xxx), Tawfik Madarati(22660392), Marvin Wipfler (22959307)')  

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
        
# Seite 3
def page3():
    st.title('Test App')
    st.write('xxx')

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

# Seitenleiste
st.sidebar.title('Navigation')
pages = {
    'Playlist Recommender': page1,
    'Test Page': page2,
    'Test App updated': page3
}
selection = st.sidebar.radio("Go to:", list(pages.keys()))

# Seiteninhalt
page = pages[selection]
page()


