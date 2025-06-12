# pip install --upgrade langchain langchain-google-google-genai streamlit

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os
import base64

os.environ['GOOGLE_API_KEY'] = "AIzaSyApdVSUZyVKrIZQY1is3meRX6fyzd2KFFI"

# Initialize Google's Gemini Model

gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

#Prompt Template

# Create Prompt Templates for translation

translate_template = """You are a very fluent translator and a polygot. translate {topic} in {language}. the translation will be used for official uses. Translate the complete text and the translation should be very polished. translate based on context of the text. The translation should be in {language}.
Please follow the following instructions:
1. Dont be offensive.
2. Ensure all content is respectful and appropriate to all audiences.



"""
translate_prompt = PromptTemplate(input_variables = ["topic", "language"], template = translate_template)

#tweet_template.format(number=3, topic="Technology Absorption", context="Development of Quadcopter with Civilian vendor named RK Industries", organisation="Indian Army", language = "English")

# Create LLM Chain using Prompt Template and Model
translate_chain = translate_prompt | gemini_model

st.set_page_config(page_title="TWEET FORGE - Redlytics Ltd", layout="centered")

#st.header("AITranslator by REDLYTICS")

st.markdown("""
    <style>
    .custom-header {
        font-size: 48px;           /* Change font size */
        color: #FF4500;            /* OrangeRed color */
        font-family: 'Impact', sans-serif;  /* Bold font */
        text-align: center;        /* Center align */
        margin-top: 5px;
        margin-bottom: 0px;
    }
    </style>
""", unsafe_allow_html=True)


# Custom styled header
st.markdown('<div class="custom-header">AI Translator</div>', unsafe_allow_html=True)

st.markdown("""
    <style>
    .custom-subheader {
        font-size: 24px;              /* Adjust font size */
        color: #FF4500;               /* Orange Red color */
        font-family: 'Verdana', sans-serif; /* Custom font */
        text-align: center;           /* Center align */
        margin-bottom: 0px;
    }
    </style>
""", unsafe_allow_html=True)

# Custom styled subheader
st.markdown('<div class="custom-subheader">by FEARLESS</div>', unsafe_allow_html=True)
#st.subheader("by FEARLESS")

st.markdown("""
    <style>
    .custom-subheader_1 {
        font-size: 24px;              /* Adjust font size */
        color: #FFFFFF;               /* White color */
        font-family: 'Verdana', sans-serif; /* Custom font */
        text-align: center;           /* Center align */
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-subheader_1">Translate using AI and reduce your reliance on Interpreter and save TIME!"</div>', unsafe_allow_html=True)
#st.subheader("Generate Tweets that has HIGH User Engagement and User Retention without disclosing YOUR IDENTITY")

# Streamlit input
topic = st.text_input('Enter the Text', "Example - India is a Democracy")
#topic = st.text_input("Topic")

#context = st.text_area('Enter CONTEXT of the TWEET',"Example - Collabaration with RK Industries development of Quadcopter as part of Make In India")
#language = st.text_input("Language")

col1, col2 = st.columns(2)

with col1:
    language = st.selectbox(label = "Choose LANGUAGE of Tweet", options = ['English','Mandarin', 'Cantonese','Hindi', 'Arabic', 'Urdu', 'Mandarin', 'Cantonese'])

with col2:
    organisation = st.text_input('Organisation', "Example - Indian Army/ Ashtashakti Command")

#with col3:
#   number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)

left, middle, right = st.columns(3)
#if left.button("Plain button", use_container_width=True):
#    left.markdown("You clicked the plain button.")
if middle.button("Translate", icon="😃", use_container_width=True):
#    middle.markdown("You clicked the emoji button.")
#if right.button("Material button", icon=":material/mood:", use_container_width=True):
#   right.markdown("You clicked the Material button.")
#if st.button("Generate Tweets"):
    #Response
    response = translate_chain.invoke({"topic" : topic, "language" : language})
    st.write(response.content)
