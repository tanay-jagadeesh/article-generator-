import requests
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import OpenAI

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

st.title("Medium Article Generator")
topic = st.text_input('Input your topic of interest')