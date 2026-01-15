import requests
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

st.title("Medium Article Generator")
topic = st.text_input('Input your topic of interest')

title_template = PromptTemplate(
    input_variables = ['topic', 'language'],
    template = 'Give me a medium article title on {topic} in {language} language'
)

llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm = llm, prompt = title_template)

if topic:
    response = title_chain.run(topic)