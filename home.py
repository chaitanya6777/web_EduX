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
        st.write("[Learn More](https://jeemain.nta.ac.in/)")

    with st.container():
        st.write("--")
        columns = st.columns(2)
        left_column = columns[0]
        right_column = columns[1]

        with left_column:
            st.header("What do we do?")
            st.write("""The JEE and NEET Prep Hub is an innovative online platform tailored to the needs of students preparing for the 
                     Joint Entrance Examination (JEE) and the National Eligibility cum Entrance Test (NEET). With an intuitive interface 
                     and a plethora of resources, our website aims to empower aspiring engineers and medical professionals to excel in these 
                     competitive exams. Students can access interactive learning modules covering all subjects, take practice tests 
                     and mock exams, and benefit from personalized study plans based on their individual strengths and weaknesses. 
                     Our platform also fosters community engagement through discussion forums and peer support groups, allowing students to 
                     collaborate with others and share valuable insights and resources. With expert guidance from experienced educators and 
                     timely updates on exam-related information, the JEE and NEET Prep Hub provides students with the tools they need to succeed 
                     and realize their academic goals.""")
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
