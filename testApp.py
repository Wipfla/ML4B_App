import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
from my_functions import getSensorData, getMetricsAcc, getMetricsGyr, getMetricsOri, getMetrics, generate_playlist, generate_video
from PIL import Image


st.set_page_config(
    page_title="BeatFit: The Data DJ",
    page_icon="🎧",
    initial_sidebar_state="expanded",
    layout="wide",
)


def predcit(df):
    # Extract Gyr Data, Acc Data, Orientation Data
    df_Acc, df_Gyr, df_Ori = getSensorData(df)

    #get metrics
    metrics_acc = getMetricsAcc(df_Acc)
    
    metrics = getMetrics(df_Acc, df_Gyr, df_Ori)
    #Load model with pickle
    model = pkl.load(open('knn.pickle', 'rb'))
    #Predict
    prediction = model.predict(metrics)
    prediction = str(prediction[0])
    return prediction

# Seite 1
def page1():

    col1, col2 = st.columns(2)

    with col1:
        st.title('🎧 BeatFit: The Data DJ - Home')
        st.subheader('Finde jetzt die passenden Playlists und Workoutvideos für deine Aktivität!')
        st.write("Willkommen bei **BeatFit**!\n")
        st.write("Hast du dich jemals gefragt, wie du deine alltäglichen Bewegungen und Aktivitäten in die ultimative Playlist verwandeln kannst? Nun, suche nicht weiter, denn BeatFit ist hier, um dein persönlicher musikalischer Begleiter zu sein!\n")

        st.write("Stell dir vor, du könntest dein Handy in einen vertrauenswürdigen DJ verwandeln, der deine Bewegungen, deine Stimmung und deine Energie erfasst und dir die perfekte Musik empfiehlt. Das ist genau das, was BeatFit für dich tun kann!\n")

        st.write("Es ist ganz einfach: Lade einfach deine Bewegungssensordaten von deinem Handy hoch, und basierend auf diesen Informationen werden wir eine speziell für dich zusammengestellte Spotify-Playlist erstellen, die perfekt zu deinem Tagesablauf, deinen Aktivitäten und deiner Stimmung passt.\n")

        st.write("Aber das ist noch nicht alles! Neben der Spotify-Playlist bietet BeatFit dir auch passende YouTube-Videos an, die deine Stimmung und Interessen widerspiegeln. Ob du nach Musikvideos, Live-Auftritten oder sogar Tanzanleitungen suchst, BeatFit hat alles im Angebot.\n")

        st.write("Also, worauf wartest du noch? Lass uns gemeinsam die Magie der Musik und der Bewegung erforschen. Lade deine Handydaten hoch, lehn dich zurück und lass BeatFit deine musikalische Reise beginnen!\n")

        st.write("Hinweis: Bei BeatFit liegt uns der Datenschutz sehr am Herzen. Alle deine hochgeladenen Daten werden anonymisiert und vertraulich behandelt. Wir nehmen deine Privatsphäre ernst und werden sie niemals ohne deine Zustimmung teilen.")
        st.write('Uploade deine Fitness Sensor Daten von deinem Handy und - Los gehts!\n' )
    
        st.info('Alexander Frey(23169187), Pierre Engel(23224488), Tawfik Madarati(22660392), Marvin Wipfler (22959307)')
    
    with col2:
        image = Image.open('data/flex.jpg')
        st.image(image, caption='Lass uns das Training starten!', use_column_width=True)

    st.info('Alexander Frey(23169187), Pierre Engel(23224488), Tawfik Madarati(22660392), Marvin Wipfler (22959307)')


# Seite 2
def page2():
    st.title('Playlist Empfehlung')
    st.subheader('Finde jetzt die perfekte Playlist, passend zu deinen Bewegungen!')

    st.markdown('**Lade deine Daten jetzt hoch und genieß die Musik !**')

    # File Uploader
    UserFile = st.file_uploader(label='Lade hier dein Json File hoch' ,type={"json"})
    if UserFile is not None:
        st.success('File erfolgreich hochgeladen!', icon="✅")
        UserFile_df = pd.read_json(UserFile)
       
        prediction = predcit(UserFile_df)
        st.write(f'Basierend auf deinen Bewegungsdaten hast du **:red[{prediction}]** gemacht!')

                
        #Korrekt? Ja/Nein
        st.subheader("War dies Korrekt?")    
        container_yes, container_no = st.columns(2)
        
        with container_yes:
            yesButton = st.button(label = 'Ja', use_container_width = 1)
            
        with container_no:
            noButton = st.button(label = 'Nein', use_container_width = 1)
                    
        if yesButton:
            st.session_state['inCorrect'] = False
            st.success("Super dann starte deine Playlist!", icon="💪")
            st.balloons()
            selected_link = generate_playlist(prediction)
            st.write(f"Hier ist deine persönlich ausgesuchte Playlist:")
            st.markdown(f"[Playlist Link]({selected_link})")

        if 'inCorrect' not in st.session_state:
            st.session_state['inCorrect'] = False
            
        if noButton or st.session_state['inCorrect']:
            st.session_state['inCorrect'] = True  
            st.subheader("Oh, kannst du uns verraten was die richtige Antwort war?")
            input1, input2, input3 = st.columns(3)
            
            with input1:
                jjButton = st.button(label = 'Jumping Jacks', use_container_width = 1)
                if jjButton:
                    st.write(f"Hier ist deine angepasste persönlich ausgesuchte Playlist:")
                    link = generate_playlist('jumpingjacks')
                    st.markdown(f"[Playlist Link]({link})")
            with input2:
                pushupButton = st.button(label = 'PushUps', use_container_width = 1)
                if pushupButton:
                    st.write(f"Hier ist deine angepasste persönlich ausgesuchte Playlist:")
                    link = generate_playlist('PushUps')
                    st.markdown(f"[Playlist Link]({link})")
            with input3:
                walkingButton = st.button(label = 'Walking', use_container_width = 1)
                if walkingButton:
                    st.write("Hier ist deine angepasste persönlich ausgesuchte Playlist:")
                    link = generate_playlist('walking')
                    st.markdown(f"[Playlist Link]({link})")

        
            
        

# Seite 3
def page3():
    st.title('Video Empfehlung')

    st.subheader('Finde jetzt das perfekte Workoutvideo, passend zu deinen Bewegungen!')
    st.markdown('**Lade deine Daten jetzt hoch und genieß das Workoutvideo !**')
    
    UserFile = st.file_uploader(label='Lade hier dein Json File hoch' ,type={"json"})
    if UserFile is not None:
        st.success('File erfolgreich hochgeladen!', icon="✅")
        UserFile_df = pd.read_json(UserFile)
        prediction = predcit(UserFile_df)
        st.write(f'Basierend auf deinen Bewegungsdaten hast du **:red[{prediction}]** gemacht!')
        videoURL = generate_video(prediction)
        st.write("Hier ist dein persönlich ausgesuchtes Workoutvideo:")
        st.video(videoURL)


# Seite 4
def page4():
        st.title('Deine Statistiken')
        st.subheader('xxxx')
        st.markdown('**xxxxx**')

        UserFile = st.file_uploader(label='Lade hier dein Json File hoch' ,type={"json"})
        if UserFile is not None:
            st.success('File erfolgreich hochgeladen!', icon="✅")
            UserFile_df = pd.read_json(UserFile)
        
            # Extract Gyr Data, Acc Data, Orientation Data
            df_Acc, df_Gyr, df_Ori = getSensorData(UserFile_df)

            #get metrics
            metrics_acc = getMetricsAcc(df_Acc)
            
            metrics = getMetrics(df_Acc, df_Gyr, df_Ori)

            #Zeige die Acc Metrics an im Dataviewer
            st.caption('Accelerometer Metrics')
            st.dataframe(metrics_acc)

            # Zeig DataFrame als Line Chart an
            st.caption('Gyroscope Data')
            st.line_chart(data=df_Gyr, x='time', y=['x', 'y', 'z'])

            # Zeig DataFrame als Line Chart an
            st.caption('Accelerometer Data')
            st.line_chart(data=df_Acc, x='time', y=['x', 'y', 'z'])



# Seitenleiste
st.sidebar.title('Navigation')
pages = {
    'Home': page1,
    'Playlist Empfehlung': page2,
    'Video Empfehlung': page3,
    'Deine Statistiken': page4
}   
selection = st.sidebar.radio("Go to:", list(pages.keys()))

# Seiteninhalt
page = pages[selection]
page()
