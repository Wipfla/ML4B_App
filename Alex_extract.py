import pandas as pd
import numpy as np
import json

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


        def extract_data(Gyr, Acc, Ori)
            if UserFile.name.endswith('.json'):
                df_gyr = pd.read_json(Gyr)
                df_acc = pd.read_json(Acc)
                df_ori = pd.read_json(Ori)
                
            else
                return false #Evtl kann man hier ne Exception werfen aber des müsste man halt machen, ne?
            