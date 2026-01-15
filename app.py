import requests
import os
from dotenv import load_dotenv
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

st.title("Medium Article Generator")
topic = st.text_input('Input your topic of interest')

title_template = PromptTemplate(
    input_variables = ['topic', 'language'],
    template = 'Give me a medium article title on {topic} in {language} language'
)

article_template = PromptTemplate(
    input_variables = ['topic', 'language'],
    template = 'Give me a medium article for title: {title}'
)

llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm = llm, prompt = title_template)

llm = ChatOpenAI(model_name = 'gpt-3.5-turbo', temperature=0.9)

article_chain = LLMChain(llm = llm, prompt = article_template, verbose = True)

overall_chain = SimpleSequentialChain(chaines = [title_chain, article_chain], verbose = True)
if topic:
    response = overall_chain.run(topic)
    st.write(response)
