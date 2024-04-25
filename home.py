import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

def app():
    lottie_image = "https://lottie.host/a05b46e6-d765-4930-80f0-b2aa67423882/j5zoYleOxL.json"
    img_iit = Image.open("images/iit.jpg")
    img_neet = Image.open("images/neet.jpg")

    with st.container():
        st.subheader("Hi, This is Team :violet[EduX] ❤️ from IIT Palakkad")
        st.title("A platform where you can prepare for JEE")
        st.write("Here you can find a lot of useful information for competitive exams like JEE")
        st.write("[Learn More](https://google.com)")

    with st.container():
        st.write("--")
        columns = st.columns(2)
        left_column = columns[0]
        right_column = columns[1]

        with left_column:
            st.header("What do we do?")
            st.write("""Saideep is a driven individual with a keen intellect and a thirst for learning. 
                     His dedication and perseverance make him a valuable asset in any endeavor he undertakes. 
                     With a natural curiosity and a passion for excellence, Saideep continually seeks 
                     opportunities for personal and professional growth. He approaches challenges with a 
                     positive attitude and a willingness to innovate, inspiring those around him to strive 
                     for greatness.""")
        with right_column:
            st_lottie(lottie_image, height=300, key="image")

    with st.container():
        st.write("--")
        st.header("Resources")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_iit)
            st.subheader("Here are details for JEE")
            st.write("Watch this to learn more")
            st.markdown("[Watch Video](https://youtube.com)")

        with text_column:
            st.image(img_neet)
            st.subheader("Here are details for NEET")
            st.write("Watch this to learn more")
            st.markdown("[Watch Video](https://youtube.com)")
