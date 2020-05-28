import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Safe boda pickups in Kampala')

DATE_COLUMN = 'date/time'

DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase,axis='columns', inplace=True)
