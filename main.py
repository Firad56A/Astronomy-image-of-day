import streamlit as st
import requests
api_key = "roNYYrEujp2OaopUwM4BwdHgcCRTzDamWvCIMWbY"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"


request = requests.get(url)

response = request.json()

print(response)
st.set_page_config(layout="wide")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.title(response["title"])
    st.image(response["hdurl"],width=600)
st.write(response["explanation"])

