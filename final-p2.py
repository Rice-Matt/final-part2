import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.header('Matt Rice final part2')

URL = "https://raw.githubusercontent.com/Rice-Matt/final-part2/main/bike_sharing.csv"
df = pd.read_csv(URL)

st.write('1.Create a line plot of total ridership (column titled cnt) over the course of the entire period')

df['dteday'] = pd.to_datetime(df['dteday'])
dates = df['dteday']
counts = df['cnt']

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, counts)
ax.set_xlabel('Date')
ax.set_ylabel('Total Ridership')
ax.set_title('Total Ridership Over Time')
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)


st.write('2.Create a bar plot that shows total ridership by season')

seasonal_ridership = df.groupby('season')['cnt'].sum()

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(seasonal_ridership.index, seasonal_ridership.values)
ax.set_xlabel('Season (1: Winter, 2: Spring, 3: Summer, 4: Fall)')
ax.set_ylabel('Total Ridership')
ax.set_title('Total Ridership by Season')
plt.xticks(seasonal_ridership.index)
plt.tight_layout()

st.pyplot(fig)

st.write('3.Create a line plot of total ridership that allows the user to select rolling average.  Using a radio button, the user can select 7-day average or a 14-day average')

avg_selection = st.radio("Select Rolling Average:", ("7-day", "14-day"))
if avg_selection == "7-day":
    rolling_avg = df['cnt'].rolling(window=7).mean()
else:
    rolling_avg = df['cnt'].rolling(window=14).mean()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['dteday'], df['cnt'], label='Original Data')
ax.plot(df['dteday'], rolling_avg, label=f'{avg_selection} Rolling Average')
ax.set_xlabel('Date')
ax.set_ylabel('Total Ridership')
ax.set_title('Total Ridership with Rolling Average')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

st.pyplot(fig)




