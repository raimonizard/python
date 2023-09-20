import pandas as pd
import matplotlib.pyplot as plt

def __init__():
  # serieA = test_serie()
  # print(serieA)
  # serieB = rename_serie(serieA)
  # print(serieB)
  #create_dic()
  df = loadFile("data\dirtydata.csv")
  clean_data_frame = data_cleansing(df)
  show_data_correlations(clean_data_frame)
  plot_data(clean_data_frame)

def test_serie():
  # Create a basic python list:
  a = [1, 7, 2]
  return a

def rename_serie(a):
  # Create a pandas.Serie from a python list:
  serieB = pd.Series(a, index = ["pepe", "maria", "juana"])
  return serieB

def create_dic():
  # Create a basic python dictionary:
  data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
    }

  # Create a Pandas.dataframe from a python dictionary:
  df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

  # Print all the dataframe:
  print(df)

  # Print "day1" series:
  print(df.loc["day1"])

def loadFile(filename):
  # Create a new Pandas.dataframe with the info in the given file:
  df = pd.read_csv(filename)

  # Shows the structure of the dataframe: its series and its data type.
  print(df.info())

  # Shows all the dataframe:
  # print(df.to_string())
  
  # Shows part of the dataframe:
  print(df)

  return df

def data_cleansing(dataframe):
  # Remove duplicated rows:
  dataframe.drop_duplicates(inplace = True)

  # Fix values for "Calories" series:
  caloriesMean = dataframe["Calories"].mean()
  dataframe["Calories"].fillna(caloriesMean, inplace=True)

  # Fix values for "Duration" series:
  durationMean = dataframe["Duration"].mean()
  durationMode = dataframe["Duration"].mode()[0]

  for i in dataframe.index:
    if dataframe.loc[i, "Duration"] > durationMean:
      dataframe.loc[i, "Duration"] = durationMode

  # Assign data format for "Date" series:
  dataframe["Date"] = pd.to_datetime(dataframe["Date"])
  dataframe.dropna(subset=["Date"], inplace=True)

  return dataframe

def show_data_correlations(dataframe):
  # Show dataframe series correlations:
  print(dataframe.corr())

  # Show the correlations on a linear graphic:
  dataframe.corr().plot()
  plt.show()

def plot_data(dataframe):
  # Prepare de pandas.dataframe to be printed:
  dataframe[["Duration", "Pulse", "Maxpulse", "Calories"]].plot()
  
  # Create a window plot wit Matplotlib:
  plt.show()


  
__init__()  