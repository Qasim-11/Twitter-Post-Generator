


import tweepy
import streamlit as st
import os
from openai import OpenAI
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
consumer_key = st.secrets["consumer_key"]
consumer_secret = st.secrets["consumer_secret"]
access_token = st.secrets["access_token"]
access_token_secret = st.secrets["access_token_secret"]

client = OpenAI(api_key = OPENAI_API_KEY)


# Function to generate text using OpenAI
def generate_text(prompt):
    TEXT = f"You are an expert in artificial intelligence and Twitter content creation. Write a concise blog post for Twitter on the topic: {prompt}. Keep it under 280 characters."
    response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content":TEXT},

  ]
  )
    return response.choices[0].message.content

def create_tweet(text):
    client = tweepy.Client(
        consumer_key= consumer_key,
        consumer_secret= consumer_secret,
        access_token= access_token,
        access_token_secret= access_token_secret
    )
    response = client.create_tweet(text=text)
    return response

# Streamlit app
def main():
    st.title('Twitter Post Generator')

    # User input for the tweet
    text = st.text_area('Enter your tweet text:')

    if st.button('Generate Tweet'):
        # Create the tweet
        create_tweet(generate_text(text))

        # Display tweet URL
        st.success(f'Tweet posted! Here is the URL for the Tweeter account : {"https://twitter.com/IAUBot224"}')

if __name__ == "__main__":
    main()

