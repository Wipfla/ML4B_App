import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
from my_functions import getSensorData, getMetricsAcc, getMetricsGyr, getMetricsOri, generate_playlist

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
    st.subheader('Finde jetzt die Perfekte Playlist, passend zu deinen Bewegungen!')

    st.markdown('**Upload your File here and be amazed!**')

    UserFile = st.file_uploader(label='Please upload a Json File' ,type={"json"})
    if UserFile is not None:
        st.success('File successfully uploaded!', icon="✅")
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
        #metrics_acc = getMetricsAcc(df_Acc)
        #st.dataframe(metrics_acc)

        if st.button("Find your Playlist"):
            selected_link = generate_playlist("JumpingJacks")
            if selected_link:
                st.success("Playlist gefunden!")
                st.write(f"Hier ist deine persönlich ausgesuchte Playlist: {selected_link}")

                if st.button("Hör direkt rein!"):
                    st.write(f"Du wirst weitergeleitet zu: {selected_link}")
            else:
                st.warning("No playlist available for the selected category.")

    # Ballons
    st.button('Click me!', on_click=st.balloons)

# Seite 3


def page3():
    st.title('Video Empfehlung')

    st.subheader('Finde jetzt das perfekte Workoutvideo, passend zu deinen Bewegungen!')


# Seitenleiste
st.sidebar.title('Navigation')
pages = {
    'Home': page1,
    'Playlist Empfehlung': page2,
    'Video Empfehlung': page3
}
selection = st.sidebar.radio("Go to:", list(pages.keys()))

# Seiteninhalt
page = pages[selection]
page()
