import streamlit as st
import datetime

from streamlit import markdown

st.title("WELCOME TO MANGOLI WEB")

st.divider()
st.image("mangoli.png", caption="by: BoZaher", use_container_width=True)
st.divider()

option = st.multiselect(
    "who is you?",
    ["MAMOUN", "KHALED"],
    placeholder="choose ya niga",)

if "MAMOUN" in option:
    st.write("hala walla")
elif "KHALED" in option:
    st.write("manglala")

st.divider()

st.camera_input("show us your face")

st.divider()

today = datetime.date.today()
st.write(today)
last_week = today - datetime.timedelta(days=7)

st.date_input(
  "select your age",
  value = (today),
  min_value = datetime.date(2008, 12, 1),
  max_value = datetime.date.today(),
  format= "MM.DD.YYYY")

st.divider()
st.write("VERY IMPORTANT QUISTION")
st.radio(
  "IS YOU NIGGA 🧐",
  ["YES", "YES"],
  captions= ["ME IS NIGA", "ME IS NIGA ALSO"]
)

markdown("---")