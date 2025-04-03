import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as math

# Title of App
st.title("Web Development Lab03")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 09, Web Development - Section B")
st.subheader("Nicholas Geller, Lillian Yan")



st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:""")

st.page_link("pages/Fruit Nutrition Analyzer.py", label= "1: Fruit Nutrition Analyzer: Using the Fruityvice Api, analyze the nutirtional content of diffrent fruits 🍓 .")
st.write("2:")
st.write("3:")
st.write("4:")


