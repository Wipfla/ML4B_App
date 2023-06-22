import pandas as pd
import random

#Function to get Accelometer, Gyroscope and Orientation Data from Json in one Dataframe each
def getSensorData(df):
    df_Acc = df[df['sensor'] == 'Accelerometer']
    df_Gyr = df[df['sensor'] == 'Gyroscope']
    df_Ori = df[df['sensor'] == 'Orientation']
  #Drop all Columns with NaN Values
    df_Acc.dropna(axis=1, how='all', inplace=True)
    df_Gyr.dropna(axis=1, how='all', inplace=True)
    df_Ori.dropna(axis=1, how='all', inplace=True)

  #Drop sensor column
    df_Acc.drop(['sensor', 'seconds_elapsed'], axis=1, inplace=True)
    df_Gyr.drop(['sensor', 'seconds_elapsed'], axis=1, inplace=True)
    df_Ori.drop(['sensor', 'seconds_elapsed'], axis=1, inplace=True)

    return df_Acc, df_Gyr, df_Ori

def getMetricsAcc(df):
  metrics = {}  # Dictionary to store the metrics for each dataframe

  metrics['Acc_mean_z'] = df['z'].mean()
  metrics['Acc_sum_z'] = df['z'].sum()
  metrics['Acc_var_z'] = df['z'].var()
  metrics['Acc_std_z'] = df['z'].std()

  metrics['Acc_mean_y'] = df['y'].mean()
  metrics['Acc_sum_y'] = df['y'].sum()
  metrics['Acc_var_y'] = df['y'].var()
  metrics['Acc_std_y'] = df['y'].std()

  metrics['Acc_mean_x'] = df['x'].mean()
  metrics['Acc_sum_x'] = df['x'].sum()
  metrics['Acc_var_x'] = df['x'].var()
  metrics['Acc_std_x'] = df['x'].std()
    
  # Append the metrics dictionary as a new row to the metrics dataframe
  Acc_metrics = pd.DataFrame(metrics, index=[0])
  
  return Acc_metrics

def getMetricsGyr(df):
  metrics = {}  # Dictionary to store the metrics for each dataframe
  
  # Calculate and store the metrics for the current dataframe
  metrics['Gyr_mean_z'] = df['z'].mean()
  metrics['Gyr_sum_z'] = df['z'].sum()
  metrics['Gyr_var_z'] = df['z'].var()
  metrics['Gyr_std_z'] = df['z'].std()

  metrics['Gyr_mean_y'] = df['y'].mean()
  metrics['Gyr_sum_y'] = df['y'].sum()
  metrics['Gyr_var_y'] = df['y'].var()
  metrics['Gyr_std_y'] = df['y'].std()

  metrics['Gyr_mean_x'] = df['x'].mean()
  metrics['Gyr_sum_x'] = df['x'].sum()
  metrics['Gyr_var_x'] = df['x'].var()
  metrics['Gyr_std_x'] = df['x'].std()

  # Add more metrics as needed
  
  # Append the metrics dictionary as a new row to the metrics dataframe
  Gyr_metrics = pd.DataFrame(metrics, index=[0])


  return Gyr_metrics

def getMetricsOri(df):

  metrics = {}  # Dictionary to store the metrics for each dataframe
  
  # Calculate and store the metrics for the current dataframe
  metrics['mean_qz'] = df['qz'].mean()
  metrics['sum_qz'] = df['qz'].sum()
  metrics['var_qz'] = df['qz'].var()
  metrics['std_qz'] = df['qz'].std()

  metrics['mean_qy'] = df['qy'].mean()
  metrics['sum_qy'] = df['qy'].sum()
  metrics['var_qy'] = df['qy'].var()
  metrics['std_qy'] = df['qy'].std()

  metrics['mean_qx'] = df['qx'].mean()
  metrics['sum_qx'] = df['qx'].sum()
  metrics['var_qx'] = df['qx'].var()
  metrics['std_qx'] = df['qx'].std()

  metrics['mean_qw'] = df['qw'].mean()
  metrics['sum_qw'] = df['qw'].sum()
  metrics['var_qw'] = df['qw'].var()
  metrics['std_qw'] = df['qw'].std()

  metrics['mean_roll'] = df['roll'].mean()
  metrics['sum_roll'] = df['roll'].sum()
  metrics['var_roll'] = df['roll'].var()
  metrics['std_roll'] = df['roll'].std()

  metrics['mean_pitch'] = df['pitch'].mean()
  metrics['sum_pitch'] = df['pitch'].sum()
  metrics['var_pitch'] = df['pitch'].var()
  metrics['std_pitch'] = df['pitch'].std()

  metrics['mean_yaw'] = df['yaw'].mean()
  metrics['sum_yaw'] = df['yaw'].sum()
  metrics['var_yaw'] = df['yaw'].var()
  metrics['std_yaw'] = df['yaw'].std()

  # Add more metrics as needed
  
  # Append the metrics dictionary as a new row to the metrics dataframe
  Ori_metrics_df = pd.DataFrame(metrics, index=[0])
  

  return Ori_metrics_df


def generate_playlist(category):
    if category == "Walk":
        links = ["https://open.spotify.com/playlist/37i9dQZF1DXdxcBWuJkbcy?si=4dc4123542854393", "https://open.spotify.com/playlist/37i9dQZF1DX9oh43oAzkyx?si=21412c4ac8074a2a", "https://open.spotify.com/playlist/37i9dQZF1DX36TRAnIL92N?si=dd1b11494a894667"]
    elif category == "JumpingJacks":
        links = ["https://open.spotify.com/playlist/37i9dQZF1DWUSyphfcc6aL?si=390d5abba5044ba2", "https://open.spotify.com/playlist/37i9dQZF1DWVceftBh0Ubl?si=9cc75fe8fa21460e", "https://open.spotify.com/playlist/37i9dQZF1DX0HRj9P7NxeE?si=7d0e961380d84026"]
    elif category == "PushUp":
        links = ["https://open.spotify.com/playlist/37i9dQZF1DX2SzDYPXnP1a?si=64c87d2fe7a64c52", "https://open.spotify.com/playlist/37i9dQZF1DXdURFimg6Blm?si=f21546256b094023", "https://open.spotify.com/playlist/37i9dQZF1EIeLflS1D0w73?si=d7eb2265d3fb4636"]
    else:
        links = []

    if links:
        selected_link = random.choice(links)
        return selected_link
    else:
        return None
    

def getMetrics(df_Acc, df_Gyr, df_Ori):
  metrics = pd.DataFrame()
  acc = getMetricsAcc(df_Acc)
  gyr = getMetricsGyr(df_Gyr)
  ori = getMetricsOri(df_Ori)
  metrics = pd.concat([acc, gyr, ori], axis=1)
  return metrics
