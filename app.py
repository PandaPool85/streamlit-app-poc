import streamlit as st
import numpy as np 
import pandas as pd 
import time 
import plotly.express as px 
import requests
import pygsheets

df = pd.read_csv('auto_df.csv')

st.set_page_config(
    page_title = 'CI Automation Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("CI Automation Dashboard")

# top-level filters 

job_filter = st.selectbox("Select the Job", pd.unique(df['Project']))

# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

df = df[df['Project']==job_filter]

event_cnt = df['Event Count'].sum() 

time_svd = df['Minutes Saved'].sum()/60
    
#balance = np.mean(df['balance_new'])

with placeholder.container():
        # create two columns, can update later with additonal KPIs
        kpi1, kpi2 = st.columns(2)

        # fill in those three columns with respective metrics or KPIs 
        kpi1.metric(label="Total Events", value=int(event_cnt), delta= int(event_cnt) - 10)
        kpi2.metric(label="Time Saved (HRs)", value= int(time_svd), delta= int(time_svd) - 10)
        #kpi3.metric(label="A/C Balance ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_married) * 100)

        # create two columns for charts 

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.bar(data_frame=df, y = 'Event Count', x = 'Month Year')
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame = df, x = 'Event Count')
            st.write(fig2)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        
    #placeholder.empty()
