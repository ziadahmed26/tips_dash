#importing libarires
import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px

st.set_page_config(page_title= "Tips dashboard" ,
                     page_icon= None ,
                     layout = "wide",
                     initial_sidebar_state="auto",
                     menu_items=None)

#loading data 
df=pd.read_csv('tips.csv')


# sidebar
st.sidebar.header("Tips dashboard")
st.sidebar.image('tips.jpeg')
st.sidebar.write("this dashboard is using tips dataset from seaborn ")
st.sidebar.write("")
st.sidebar.write("filter your data")
cat_filter=st.sidebar.selectbox("categorical", [ None,'Sex', 'Smoker', 'Day', 'Time'])
num_filter=st.sidebar.selectbox("numerical", [ None,'Total_bill','Tip'])
row_filter=st.sidebar.selectbox("Row filtering", [ None,'Sex', 'Smoker', 'Day', 'Time'])
col_filter=st.sidebar.selectbox("Col filtering", [ None,'Sex', 'Smoker', 'Day', 'Time'])


st.sidebar.write("")
st.sidebar.markdown("made with :heart_eyes: by  Eng.[Ziad Ahmed](https://www.linkedin.com/in/ziad-ahmed-061828238/)")

#body

#row a
a1,a2,a3,a4=st.columns(4)

a1.metric("Max. Total bill",df['Total_bill'].max())
a2.metric("Max. Tip ",df['Tip'].max())
a3.metric("Min. Total bill",df['Total_bill'].min())
a4.metric("Min. Tip",df['Tip'].min())

#row b
st.subheader("Total Bills vs. Tips")
fig=px.scatter(data_frame=df,
               x='Total_bill',
               y='Tip',
               color=cat_filter,
               size=num_filter,
               facet_col=col_filter,
               facet_row=row_filter)
st.plotly_chart(fig,use_container_width=True)

#row c 
c1, c2, c3 =st.columns((4,3,3))
with c1:
     st.text("Sex vs. Total Bills ")
     fig=px.bar(data_frame=df,x='Sex',
               y='Total_bill',
               color=cat_filter)
     st.plotly_chart(fig,use_container_width=True)

with c2:
    st.text("Smoker/Non smoker vs. Tips ")
    fig=px.pie(data_frame=df,
               names='Smoker',
               values='Tip',
               color=cat_filter)
    st.plotly_chart(fig,use_container_width=True)

with c3:
     st.text("Days vs. Tips ")
     fig=px.pie(data_frame=df,
               names='Day',
               values='Tip',
               color=cat_filter,
               hole=0.4)
     st.plotly_chart(fig, use_container_width=True)
     



