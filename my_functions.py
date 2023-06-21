import pandas as pd

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
  Acc_metrics = pd.DataFrame()
  metrics = {}  # Dictionary to store the metrics for each dataframe

  Acc_metrics['mean_z'] = df['z'].mean()
  Acc_metrics['sum_z'] = df['z'].sum()
  Acc_metrics['var_z'] = df['z'].var()
  Acc_metrics['std_z'] = df['z'].std()

  Acc_metrics['mean_y'] = df['y'].mean()
  Acc_metrics['sum_y'] = df['y'].sum()
  Acc_metrics['var_y'] = df['y'].var()
  Acc_metrics['std_y'] = df['y'].std()

  Acc_metrics['mean_x'] = df['x'].mean()
  Acc_metrics['sum_x'] = df['x'].sum()
  Acc_metrics['var_x'] = df['x'].var()
  Acc_metrics['std_x'] = df['x'].std()

  

  return Acc_metrics

def getMetricsGyr(df):
  Gyr_metrics = pd.DataFrame()

  metrics = {}  # Dictionary to store the metrics for each dataframe
  
  # Calculate and store the metrics for the current dataframe
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

  # Add more metrics as needed
  
  # Append the metrics dictionary as a new row to the metrics dataframe
  Gyr_metrics = Gyr_metrics.append(metrics, ignore_index=True)


  return Gyr_metrics

def getMetricsOri(df):
  Ori_metrics_df = pd.DataFrame()

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
  Ori_metrics_df = Ori_metrics_df.append(metrics, ignore_index=True)
  

  return Ori_metrics_df
