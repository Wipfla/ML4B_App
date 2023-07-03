import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
from my_functions import getSensorData, getMetricsAcc, getMetricsGyr, getMetricsOri, getMetrics, generate_playlist, generate_video, create_combined_histogram, create_combined_scatter_plot
from PIL import Image
from streamlit import session_state as state


st.set_page_config(
    page_title="BeatFit: The Data DJ",
    page_icon="🎧",
    initial_sidebar_state="expanded",
    layout="wide",
)


def predcit(df):
    # Extract Gyr Data, Acc Data, Orientation Data
    df_Acc, df_Gyr, df_Ori = getSensorData(df)

    # Get Metrics for each Dataframe
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

        st.write("Aber das ist noch nicht alles! Neben der Spotify-Playlist sucht BeatFit dir auch passende YouTube-Workout-Videos raus, die zu deinen Bewegungne passen.\n")

        st.write("Also, worauf wartest du noch? Lass uns gemeinsam die Magie der Musik und der Bewegung erforschen. Lade deine Handydaten hoch, lehn dich zurück und lass BeatFit deine musikalische Reise beginnen!\n")

        st.write("Hinweis: Bei BeatFit liegt uns der Datenschutz sehr am Herzen. Alle deine hochgeladenen Daten werden anonymisiert und vertraulich behandelt. Wir nehmen deine Privatsphäre ernst und werden sie niemals ohne deine Zustimmung teilen.")
        st.write('Uploade deine Fitness Sensor Daten von deinem Handy und - Los gehts!\n' )
    
        st.info('Alexander Frey(23169187), Pierre Engel(23224488), Tawfik Madarati(22660392), Marvin Wipfler (22959307)')
    
    with col2:
        image = Image.open('data/flex.jpg')
        st.image(image, caption='Lass uns das Training starten!', use_column_width=True)


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

        state.prediction = None 
                   
        if yesButton:
            st.session_state['inCorrect'] = False
            st.success("Super dann starte deine Playlist!", icon="💪")
            st.balloons()
            selected_link = generate_playlist(prediction)
            st.write(f"Hier ist deine persönlich ausgesuchte Playlist:")
            st.markdown(f"[Playlist Link]({selected_link})")
            state.prediction = prediction

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
                    prediction = 'jumpingjacks'
                    state.prediction = prediction
            with input2:
                pushupButton = st.button(label = 'PushUps', use_container_width = 1)
                if pushupButton:
                    st.write(f"Hier ist deine angepasste persönlich ausgesuchte Playlist:")
                    link = generate_playlist('pushups')
                    st.markdown(f"[Playlist Link]({link})")
                    prediction = 'PushUps'
                    state.prediction = prediction
            with input3:
                walkingButton = st.button(label = 'Walking', use_container_width = 1)
                if walkingButton:
                    st.write("Hier ist deine angepasste persönlich ausgesuchte Playlist:")
                    link = generate_playlist('walking')
                    st.markdown(f"[Playlist Link]({link})")
                    prediction = 'walking'
                    state.prediction = prediction

        
            
        

# Seite 3
def page3():
    st.title('Video Empfehlung')

    st.subheader('Finde jetzt das perfekte Workoutvideo, passend zu deinen Bewegungen!')
    st.markdown('**Lade deine Daten jetzt hoch und genieß das Workoutvideo !**')
    
    UserFile = st.file_uploader(label='Lade hier dein Json File hoch' ,type={"json"})
    if UserFile is not None:
        st.success('File erfolgreich hochgeladen!', icon="✅")
        UserFile_df = pd.read_json(UserFile)
        transferred_prediction = state.prediction
        if transferred_prediction is None:
            st.warning('Bitte bestätige zuerst ob die Vorhersage korrekt war!' , icon="⚠️")
        else:
            st.write(f'Basierend auf deinen Bewegungsdaten hast du **:red[{transferred_prediction}]** gemacht!')
            videoURL = generate_video(transferred_prediction)
            st.write("Hier ist dein persönlich ausgesuchtes Workoutvideo:")
            st.video(videoURL)


# Seite 4
def page4():
        st.title('Deine Statistiken')

        st.subheader('Finde heraus, wie deine Daten aussehen!')
        st.markdown('**Lade deine Daten jetzt hoch und genieß die Statistiken !**')

        UserFile = st.file_uploader(label='Lade hier dein Json File hoch' ,type={"json"})
        if UserFile is not None:
            st.success('File erfolgreich hochgeladen!', icon="✅")
            UserFile_df = pd.read_json(UserFile)
            transferred_prediction = state.prediction
            if transferred_prediction is None:
                st.warning('Bitte bestätige zuerst ob die Vorhersage korrekt war!' , icon="⚠️")
            else:
                st.write(f'Basierend auf deinen Bewegungsdaten hast du **:red[{transferred_prediction}]** gemacht!')

                # Extract Gyr Data, Acc Data, Orientation Data
                df_Acc, df_Gyr, df_Ori = getSensorData(UserFile_df)

                #get metrics
                metrics_acc = getMetricsAcc(df_Acc)
                

                #Zeige die Acc Metrics an im Dataviewer
                st.caption('Accelerometer Metrics')
                st.dataframe(metrics_acc)

                gyro_max = np.max(df_Gyr)
                gyro_min = np.min(df_Gyr)
                gyro_med = np.median(df_Gyr)
                gyro_mean= np.mean(df_Gyr)
                acc_max= np.max(df_Acc)
                acc_min= np.min(df_Acc)
                acc_med= np.median(df_Acc)
                acc_mean= np.mean(df_Acc)
                options = ["Bitte Suche dir eine Statistik heraus", "Maximale Höhe", "Minimale Höhe", "Höhe im Mittelwert", "Höhe im Median", "Maximale Beschleunigung", "Minimale Beschleunigung", "Beschleunigung im Mittelwert", "Beschleunigung im Median"]
                selected_option = st.selectbox('Was willst du herausfinden?', options)
                if selected_option == "Bitte Suche dir eine Statistik heraus":
                    st.write('Bitte wähle eine Option')
                elif selected_option == "Maximale Höhe":
                    st.write('Maximale Höhe: ', gyro_max)
                elif selected_option == "Minimale Höhe":
                    st.write('Minimale Höhe: ', gyro_min)
                elif selected_option == "Höhe im Mittelwert":
                    st.write('Höhe im Mittelwert: ', gyro_mean)
                elif selected_option == "Höhe im Media":
                    st.write('Höhe im Median: ', gyro_med)
                elif selected_option == "Maximale Beschleunigung":
                    st.write('Maximale Beschleunigung: ', acc_max)
                elif selected_option == "Minimale Beschleunigung":
                    st.write('Minimale Beschleunigung: ', acc_min)
                elif selected_option == "Beschleunigung im Mittelwert":
                    st.write('Beschleunigung im Mittelwert: ', acc_mean)
                elif selected_option == "Beschleunigung im Median":
                    st.write('Beschleunigung im Median: ', acc_med)
                else:
                    st.write("Please select an option.")


                option = st.selectbox('Wähle deinen Sensor', ("Beschleunigungssensor","Gyroscope"))
                tab1, tab2, tab3, tab4 = st.tabs(["Datenverständnis", "Area Chart", "Scatter Plot", "Historgamm"])
                if option =="Beschleunigungssensor":

                    with tab1:
                        st.header("So liest du deine Daten:") 
                        st.write("x: Beschleunigung (von deinem Handy aus) nach links und rechts")
                        st.write("y: Beschleunigung (von deinem Handy aus) nach vorne und hinten")
                        st.write("z: Beschleunigung (von deinem Handy aus) nach oben und unten")
                    with tab2:
                        st.header("Area Chart deiner Beschleunigungsdaten")
                        tab2.area_chart(data=df_Acc, x='time', y=['x', 'y', 'z'])
                    with tab3:
                        st.header("Scatter Plot deines Beschleunigungssensor")
                        create_combined_scatter_plot([df_Acc['x'], df_Acc['y'], df_Acc['z']])
                    with tab4:
                        tab4.header("Histogramm deiner Beschleunigungsdaten")
                        create_combined_histogram([df_Acc['x'], df_Acc['y'], df_Acc['z']])

                elif option == "Gyroscope":
                    with tab1:
                        st.header("So liest du deine Daten:") 
                        st.write("x: Neigung des Handys entlang der Querachse")
                        st.write("y: Neigung des Handys entlang der Längsache")
                        st.write("z: Rotieren des Handys am Mittelpunkt")
                    with tab2:
                        st.header("Area Chart deiner Gyroscopedaten")
                        tab2.area_chart(data=df_Gyr, x='time', y=['x', 'y', 'z'])
                    with tab3:
                        tab3.header("Scatter Plot deines Gyroscopedaten")
                        create_combined_scatter_plot([df_Gyr['x'], df_Gyr['y'], df_Gyr['z']])
                    with tab4:
                        tab4.header("Histogramm deiner Gyroscopedaten")
                        create_combined_histogram([df_Gyr['x'], df_Gyr['y'], df_Gyr['z']])
                    












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
