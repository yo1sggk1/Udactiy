# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import pandas as pd, csv
import numpy as np
import datetime
from matplotlib import pyplot as plt

% matplotlib inline
# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html
df = pd.read_csv("PlayersData.csv")
df.head()
current_day = datetime.datetime.now().date()
df.birthday = df.birthday.str[:10]

df['current_date'] = current_day


df.current_date = df.current_date.apply(pd.to_datetime)
df.birthday = df.birthday.apply(pd.to_datetime)
df['age'] = datetime.timedelta(df.current_date - df.birthday) 
"""
def getAge(birthday):
    today = pd.to_datetime(df.current_date).astype(int)
    birthday = pd.to_datetime(df.birthday).astype(int)
    return (today - birthday) / 10000

df['age'] = df['birthday'].apply(lambda date: getAge(date))
df['age'] = df.current_date - df.birthday
df.head()
"""
