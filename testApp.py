import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
from my_functions import getSensorData, getMetricsAcc, getMetricsGyr, getMetricsOri, getMetrics, generate_playlist, generate_video


st.set_page_config(
    page_title="TuneTracker: The Data DJ",
    page_icon="🎧",
    initial_sidebar_state="expanded",

)

# Seite 1
def page1():
    st.title('🎧 TuneTracker: The Data DJ - Home')
    st.subheader('Finde jetzt die passenden Playlists und Workoutvideos für deine Aktivität!')
    st.write("Willkommen bei **TuneTracker**!\n")
    st.write("Hast du dich jemals gefragt, wie du deine alltäglichen Bewegungen und Aktivitäten in die ultimative Playlist verwandeln kannst? Nun, suche nicht weiter, denn TuneTracker ist hier, um dein persönlicher musikalischer Begleiter zu sein!\n")

    st.write("Stell dir vor, du könntest dein Handy in einen vertrauenswürdigen DJ verwandeln, der deine Bewegungen, deine Stimmung und deine Energie erfasst und dir die perfekte Musik empfiehlt. Das ist genau das, was TuneTracker für dich tun kann!\n")

    st.write("Es ist ganz einfach: Lade einfach deine Bewegungssensordaten von deinem Handy hoch, und basierend auf diesen Informationen werden wir eine speziell für dich zusammengestellte Spotify-Playlist erstellen, die perfekt zu deinem Tagesablauf, deinen Aktivitäten und deiner Stimmung passt.\n")

    st.write("Bist du morgens eine dynamische Kraft? Kein Problem! TuneTracker wird dir eine Playlist liefern, die dich auf Trab hält und dir den perfekten Energieschub für den Tag gibt. Oder vielleicht möchtest du nach einem langen Tag der Arbeit entspannen und abschalten? TuneTracker wird dir sanfte Klänge und ruhige Melodien bieten, um dich zu beruhigen und zu erholen.\n")

    st.write("Aber das ist noch nicht alles! Neben der Spotify-Playlist bietet TuneTracker dir auch passende YouTube-Videos an, die deine Stimmung und Interessen widerspiegeln. Ob du nach Musikvideos, Live-Auftritten oder sogar Tanzanleitungen suchst, TuneTracker hat alles im Angebot.\n")

    st.write("Also, worauf wartest du noch? Lass uns gemeinsam die Magie der Musik und der Bewegung erforschen. Lade deine Handydaten hoch, lehn dich zurück und lass TuneTracker deine musikalische Reise beginnen!\n")

    st.write("Hinweis: Bei TuneTracker liegt uns der Datenschutz sehr am Herzen. Alle deine hochgeladenen Daten werden anonymisiert und vertraulich behandelt. Wir nehmen deine Privatsphäre ernst und werden sie niemals ohne deine Zustimmung teilen.")
    st.write('Uploade deine Fitness Sensor Daten von deinem Handy und - Los gehts!\n' )
    

    

    st.info('Alexander Frey(23169187), Pierre Engel(23224488), Tawfik Madarati(22660392), Marvin Wipfler (22959307)')


# Seite 2
def page2():
    st.title('Playlist Empfehlung')
    st.subheader('Finde jetzt die perfekte Playlist, passend zu deinen Bewegungen!')

    st.markdown('**Lade deine Daten jetzt hoch und genieß die Musik !**')

    UserFile = st.file_uploader(label='Lade hier dein Json File hoch' ,type={"json"})
    if UserFile is not None:
        st.success('File erfolgreich hochgeladen!', icon="✅")
        UserFile_df = pd.read_json(UserFile)
        # Extract Gyr Data, Acc Data, Orientation Data
        df_Acc, df_Gyr, df_Ori = getSensorData(UserFile_df)
        # Zeig DataFrame als Line Chart an
        st.caption('Gyroscope Data')
        st.line_chart(data=df_Gyr, x='time', y=['x', 'y', 'z'])

        # Zeig DataFrame als Line Chart an
        st.caption('Accelerometer Data')
        st.line_chart(data=df_Acc, x='time', y=['x', 'y', 'z'])

        #get metrics
        metrics_acc = getMetricsAcc(df_Acc)
        
        metrics = getMetrics(df_Acc, df_Gyr, df_Ori)

        #Zeige die Acc Metrics an im Dataviewer
        st.caption('Accelerometer Metrics')
        st.dataframe(metrics_acc)


        #Load model with pickle
        model = pkl.load(open('knn.pickle', 'rb'))
        #Predict
        prediction = model.predict(metrics)
        prediction = str(prediction[0])
        st.write('Basierend auf deinen Bewegungsdaten hast du ', prediction, ' gemacht!')

        #predictedCategory ="jumpingjacks"

        if st.button("Finde meine neue Playlist"):
            selected_link = generate_playlist(prediction)
            if selected_link:
                st.success("Playlist gefunden!")
                st.write(f"Hör gerne rein: {selected_link}")
                
            else:
                st.warning("No playlist available for the selected category.")

    

# Seite 3


def page3():
    st.title('Video Empfehlung')

    st.subheader('Finde jetzt das perfekte Workoutvideo, passend zu deinen Bewegungen!')
    st.markdown('**Lade deine Daten jetzt hoch und genieß das Workoutvideo !**')

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


        #Load model with pickle
        model = pkl.load(open('knn.pickle', 'rb'))
        #Predict
        prediction = model.predict(metrics)
        prediction = str(prediction[0])
        st.write('Basierend auf deinen Bewegungsdaten hast du ', prediction, ' gemacht!')
    # Ballons
    st.button('Click me!', on_click=st.balloons)
    

    if st.button("Finde meinen neuen Trainingspartner"):
            selected_link = generate_video(prediction)
            if selected_link:
                st.success("Trainingspartner gefunden!")
                st.write(f"Hier ist deine persönlich ausgesuchter Trainingspartner: {selected_link}")
            else:
                st.warning("No playlist available for the selected category.")



def page4():
    st.title('Workout Statistiken')

    st.subheader('Wie performst du?')
    st.markdown('**Lade deine Daten jetzt hoch und sehe deine Statistiken !**')

    UserFile = st.file_uploader(label='Lade hier dein Json File hoch' ,type={"json"})
    if UserFile is not None:
        st.success('File erfolgreich hochgeladen!', icon="✅")
        UserFile_df = pd.read_json(UserFile)
        # Extract Gyr Data, Acc Data, Orientation Data
        df_Acc, df_Gyr, df_Ori = getSensorData(UserFile_df)
    

        #get metrics
        metrics_acc = getMetricsAcc(df_Acc)
        
        metrics = getMetrics(df_Acc, df_Gyr, df_Ori)

        gyro_max = np.max(df_Gyr)
        gyro_min = np.min(df_Gyr)
        gyro_med = np.median(df_Gyr)
        gyro_mean= np.mean(df_Gyr)
        acc_max= np.max(df_Acc)
        acc_min= np.min(df_Acc)
        acc_med= np.median(df_Acc)
        acc_mean= np.mean(df_Acc)
        with st.container():
            st.write('Maximale Höhe: ', gyro_max)
        with st.container():
            st.write('Minimale Höhe: ', gyro_min)
        with st.container():
            st.write('Höhe im Mittelwert: ', gyro_mean)
        with st.container():
            st.write('Höhe im Median: ', gyro_med)

        with st.container():
            st.write('Maximale Beschleunigung: ', acc_max)
        with st.container():
            st.write('Minimale Beschleunigung: ', acc_min)
        with st.container():
            st.write('Beschleunigung im Mittelwert: ', acc_mean)
        with st.container():
            st.write('Beschleunigung im Median: ', acc_med)

        options = ["Maximale Höhe", "Minimale Höhe", "Höhe im Mittelwert", "Höhe im Median", "Maximale Beschleunigung", "Minimale Beschleunigung", "Beschleunigung im Mittelwert", "Beschleunigung im Median"]
        selected_option = st.selectbox('Was willst du herausfinden?', options)

        if selected_option == "Maximale Höhe":
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