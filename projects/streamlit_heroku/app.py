import streamlit as st
import pandas as pd
import numpy as np
import os


# Assuming 'image.jpg' is in the same directory as app.py
image_path = os.path.join(os.getcwd(), 'image.jpg')
audio_path = os.path.join(os.getcwd(), 'audio.mp3')
video_path = os.path.join(os.getcwd(), 'video.mp4')


st.title('Hello Streamlit!')
st.write('This is my first Streamlit app.')

st.header('Header')
st.subheader('Subheader')
st.text('This is some text.')


if st.button('Say hello'):
    st.write('Hello!')

name = st.text_input('Enter your name')
st.write(f'Hello, {name}')


col1, col2 = st.columns(2)
col1.write('Study Hours')
col2.write('Marks Obtained')




df = pd.DataFrame(np.random.randn(10, 3), columns=['a', 'b', 'c'])
st.line_chart(df)

st.image(image_path, caption='Sample Image')
st.audio(audio_path)
st.video(video_path)
