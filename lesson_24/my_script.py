
import pandas as pd
import streamlit as st
import plotly.express as px

from pathlib import Path

csv_path = Path(__file__).parent / "Advertising_F.csv"
df = pd.read_csv(csv_path)
st.title('Advertising Effectivness Riley')

st.sidebar.header('Filters')
x_var=st.selectbox('X axis',['TV','radio','newspaper'])

#show scatterplot
fig=px.scatter(df,x=x_var,y='sales',
           labels={'TV':'TV add spend','radio':'Radio add spend'})
st.plotly_chart(fig)

#show barplot
sales_per_city=df.groupby('City')['sales'].sum().reset_index()
fig=px.bar(sales_per_city,x='City',y='sales',title='data is fun')
st.plotly_chart(fig)

#Show dataframf
st.dataframe(df)
