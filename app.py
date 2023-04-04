import streamlit as st
import time
import os
import urllib.request
import openai as op
from openai.api_resources import engine
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Use the OpenAI API key from the environment variable

openai_api_key = st.secrets['openai']["OPENAI_API_KEY"]
if not openai_api_key:
    st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
else:

    heading='Text-to-Image Converter using  DALL-E'
    st.markdown(f"<h1 style='text-align: center'>{heading}</h1>", unsafe_allow_html=True)
    text=st.text_input('Enter the text')
    if st.button('Genereate Images'):
        
        st.info('Wait for few seconds!!')
        
        text1=text
        
        response=op.Image.create(

        prompt=text,
        n=4,
        size='1024x1024'
        
        )
        progress_bar = st.progress(0.0)
        status_text = st.empty()

        for i in range(100):
            progress_bar.progress((i + 1) / 100)
            status_text.text(f"Processing {i+1}%")
            time.sleep(0.01) # Add a delay to simulate processing time
        
        image_url1=response['data'][0]['url']
        image_url2=response['data'][1]['url']
        image_url3=response['data'][2]['url']
        image_url4=response['data'][3]['url']
        
        st.markdown(f"<h5 style='text-align: center; color:red'>{text1}</h5>", unsafe_allow_html=True)
        cols = st.columns(2)

    
        
        

        with cols[0]:
            image1=st.image(image_url1)
            st.download_button("Download Image 1", data="image1",file_name='image1.jpg', mime="image/jpg")

            image2=st.image(image_url2)
            st.download_button("Download Image 2", data="image2",file_name='image2.jpg', mime="image/jpg")
        with cols[1]:
            image3=st.image(image_url3)
            st.download_button("Download Image 3", data="image3",file_name='image3.jpg', mime="image/jpg")
            
            image4=st.image(image_url4)
            st.download_button("Download Image 4", data="image4",file_name='image4.jpg', mime="image/jpg")
