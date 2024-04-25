import streamlit as st

def app():
    st.header("Contact Us")
    left_column, _ = st.columns(2)
    with left_column:
        contact_form = """<form action="https://formsubmit.co/alchemist999.c@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <label for="name">Your Name:</label><br>
             <input type="text" id="name" name="name" required><br>
             <label for="email">Your Email:</label><br>
             <input type="email" id="email" name="email" required><br>
             <label for="message">Your Message:</label><br>
             <textarea id="message" name="message" required></textarea><br>
             <button type="submit">Submit</button>
        </form>"""
        st.markdown(contact_form, unsafe_allow_html=True)
