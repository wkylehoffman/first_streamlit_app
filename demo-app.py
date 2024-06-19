import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.set_page_config(
    page_title="Natural State Data",
    layout="wide",
    initial_sidebar_state="expanded"
)

streamlit.title("bar chart")


data = pandas.read_json('https://data.bts.gov/resource/crem-w557.json')

streamlit.line_chart(
    data=data[['date','auto_sales']], 
    x='date', 
    y='auto_sales'
    )