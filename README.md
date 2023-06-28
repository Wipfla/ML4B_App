# BeatFit - Der Daten-DJ

## Überblick
BeatFit ist eine interaktive Streamlit-App, die dazu dient, Ihren Fitness- und Gesundheitsbedarf zu erfüllen. Mit dieser App können Sie die Sensordaten von Ihrem Handy hochladen, und sie erkennt automatisch, welche Aktivität Sie gerade ausgeführt haben, ob es sich um JumpingJacks, PushUps oder Walking handelt. Basierend auf dieser Vorhersage schlägt die App eine passende Spotify-Playlist und ein passendes YouTube-Workout-Video vor, um Ihnen zu helfen, Ihre Fitnessziele zu erreichen und zu übertreffen. Darüber hinaus können Sie eine Seite mit statistischen Daten zu Ihren Bewegungsdaten einsehen, die Ihnen dabei helfen, Ihre Fortschritte zu verfolgen und Ihre Ziele anzupassen.

## Funktionen
- Aktivitätserkennung: Laden Sie Ihre Sensordaten hoch, und die App sagt voraus, welche Aktivität Sie durchgeführt haben.

- Musikempfehlung: Basierend auf Ihrer Aktivität erhalten Sie eine passende Spotify-Playlist, die Ihnen hilft, Ihre Trainingsstimmung aufrechtzuerhalten.

- Workout-Video-Empfehlung: Die App schlägt ein passendes YouTube-Workout-Video vor, das Ihrer erkannten Aktivität entspricht.

- Statistikseite: Sehen Sie statistische Daten zu Ihren Bewegungsdaten ein und verfolgen Sie Ihre Fortschritte.

## Installation
Sie benötigen Python 3.7 oder höher, um BeatFit zu verwenden. Um die App zu installieren, führen Sie die folgenden Schritte aus:


1. Klonen Sie dieses Repository:
```ruby
git clone https://github.com/Wipfla/ML4B_App.git
```
2. Wechseln Sie in das Verzeichnis ML4B_App:
```ruby
cd ML4B_App
```
3. Installieren Sie die notwendigen Python-Pakete:
```ruby
pip install -r requirements.txt
```

## Anwendung
Um die App auszuführen, verwenden Sie den folgenden Befehl im Terminal:
```ruby
streamlit run testApp.py
```

Sobald die App läuft, folgen Sie den Anweisungen auf dem Bildschirm, um Ihre Sensordaten hochzuladen und die App zu nutzen. Sie werden aufgefordert, eine JSON-Datei mit Sensordaten von Ihrem Handy hochzuladen. Für optimale Ergebnisse empfehlen wir, eine Datei mit etwa 10-30 Sekunden an Sensordaten bereitzustellen. Sie können die Datei `PushUps-Alex-Test.json` in diesem Repository verwenden, um die App zu testen.