import streamlit as st

import numpy as np
import pandas as pd
import datetime
import requests

# '''
# # TaxiFareModel front
# '''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

'## Taxi Fare prediction:'
'Please key in the following details:'

d = st.date_input(
    "Today's date",
    datetime.date(2021, 11, 12))

t = st.time_input('Current Time', datetime.time(8, 45))

mydatetime = datetime.datetime.combine(d, t)

pickup_long = st.number_input('Insert pickupp longitude')
pickup_lat = st.number_input('Insert pickup latitude')
dropoff_long = st.number_input('Insert dropoff longitude')
dropoff_lat = st.number_input('Insert dropoff latitude')

p = int(st.number_input('Insert number of passengers'))


# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://model2-u5x4kc4keq-ew.a.run.app/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

    #st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


payload = {'pickup_datetime': mydatetime , 'pickup_longitude': pickup_long, 'pickup_latitude': pickup_lat, 
           "dropoff_longitude": dropoff_long, "dropoff_latitude": dropoff_lat, "passenger_count": p}

r = requests.get(url, params=payload)
data = r.json()

'Results:'
data['prediction']

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''