import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
from my_functions import getSensorData, getMetricsGyr, getMetricsOri

def getMetricsAcc(df):
  Acc_metrics = pd.DataFrame()
  metrics = {}  # Dictionary to store the metrics for each dataframe

  metrics['mean_z'] = df['z'].mean()
  metrics['sum_z'] = df['z'].sum()
  metrics['var_z'] = df['z'].var()
  metrics['std_z'] = df['z'].std()

  metrics['mean_y'] = df['y'].mean()
  metrics['sum_y'] = df['y'].sum()
  metrics['var_y'] = df['y'].var()
  metrics['std_y'] = df['y'].std()

  metrics['mean_x'] = df['x'].mean()
  metrics['sum_x'] = df['x'].sum()
  metrics['var_x'] = df['x'].var()
  metrics['std_x'] = df['x'].std()

 # Append the label column from the current dataframe to the metrics dictionary
  metrics['activity'] = df['activity']
    
  # Append the metrics dictionary as a new row to the metrics dataframe
  Acc_metrics = Acc_metrics.append(metrics, ignore_index=True)

  #change activity to string
  Acc_metrics['activity'] = Acc_metrics['activity'].astype(str)
  #short string to 10 characters
  Acc_metrics['activity'] = Acc_metrics['activity'].str[:21]
  #delete all numbers from string
  Acc_metrics['activity'] = Acc_metrics['activity'].str.replace('\d+', '')
  #detelte all empty spaces
  Acc_metrics['activity'] = Acc_metrics['activity'].str.replace(' ', '')
  return Acc_metrics


# Seite 1
def page1():
    st.subheader('Playlist Recommender')
    # Fügen Sie hier den Inhalt der Seite 1 hinzu
    #
    st.title('Find the right Playlist for your Activity!')
    st.write('Welcome to the ultimate workout companion! Are you tired of sifting through endless playlists, trying to find the perfect tunes to fuel your exercise routine? Look no further, because our innovative Streamlit app is here to revolutionize your fitness journey.')
    st.write('Just upload your fitness data and we will find the right playlist for you!')
    

    UserFile = st.file_uploader(
        "Upload your File here and be amazed!", type={"json"})
    if UserFile is not None:
        UserFile_df = pd.read_json(UserFile)
        # Extract Gyr Data, Acc Data, Orientation Data
        df_Acc, df_Gyr, df_Ori = getSensorData(UserFile_df)
        # Zeig DataFrame als Line Chart an
        st.caption('Gyroscope Data')
        st.line_chart(data=df_Gyr, x='time', y=['x', 'y', 'z'])

        # Zeig DataFrame als Line Chart an
        st.caption('Accelerometer Data')
        st.line_chart(data=df_Acc, x='time', y=['x', 'y', 'z'])

        #Zeige die Acc Metrics an im Dataviewer
        st.caption('Accelerometer Metrics')
        metrics_acc = getMetricsAcc(df_Acc)
        st.dataframe(metrics_acc)


        st.write("Check out this [amazing Playlist for you!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)") 
     # Hier müssen wir noch den Algo einbauen für die Playlist und vlt einen Button der dich zur Playlist weiterleitet


    

    st.info('Alexander Frey(23169187), Pierre Engel(23224488), Tawfik Madarati(22660392), Marvin Wipfler (22959307)')


# Seite 2
def page2():
    st.subheader('Test Page')
    # Fügen Sie hier den Inhalt der Seite 2 hinzu
    st.title('Test Page for messing around!')
  

    # Ballons
    st.button('Click me!', on_click=st.balloons)


    # Frage
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
    st.subheader('Playlist Recommender Test')

    st.title('Find the right Playlist for your Activity!')

    st.write('Just upload your data and we will find the right playlist for you!')
    UserFile = st.file_uploader(
        "Upload your File here and be amazed!", type={"csv", "json"})
    if UserFile is not None:
        UserFile_df = pd.read_csv(UserFile)
        # Zeig DataFrame im DataFrame-Viewer an
        st.dataframe(UserFile_df)

# ToDo: ALEX
        # Extract Gyr Data, Acc Data, Orientation Data if user file is a json file
        # if UserFile.name.endswith('.json'):
        # hier muss noch eine Funktion gebaut werden die die Daten aus dem json file extrahiert (siehe test.ipynb)
        # die einzelnen Tabellen müssen dann noch in die Datenbank geladen werden bzw. concateniert werden

        # alternativ können wir noch eine Funktion bauen die die Daten aus dem json file extrahiert und dann in ein csv file umwandelt
        # dann können wir die csv file einfach in ein dataframe laden und dann weiterverarbeiten, so ungefähr:
        # def json_to_csv(file):
        #     df = pd.read_json(file)
        #     df.to_csv('data.csv', index=False)
        #     return df

        # Zeig DataFrame als Line Chart an
        st.caption('Your Gyroscope Data in Lines! WOW!')
        st.line_chart(data=UserFile, x='time', y=['x', 'y', 'z'])

     # Hier müssen wir noch den Algo einbauen für die Playlist und vlt einen Button der dich zur Playlist weiterleitet


# Seitenleiste
st.sidebar.title('Navigation')
pages = {
    'Playlist Recommender': page1,
    'Test Page': page2,
    'Playlist Test': page3
}
selection = st.sidebar.radio("Go to:", list(pages.keys()))

# Seiteninhalt
page = pages[selection]
page()
