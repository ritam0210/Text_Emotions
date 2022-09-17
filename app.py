import streamlit as st
import joblib

#import joblib model
model = joblib.load('tweet_emotions')

st.title('TWEET EMOTIONS CLASSIFIER')#creates a title in web app
ip = st.text_input('Enter the tweet') #creates a text box in web app

op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0]) # st.button will create a button with name Predict
