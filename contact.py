import streamlit as st

def app():
    st.header("Contact Us")
    left_column, _ = st.columns(2)
    with left_column:
        contact_form = """
        <style>
        input[type=message], input[type=email], input[type=text], textarea {
          width: 100%; /* Full width */
          padding: 12px; /* Some padding */ 
          border: 1px solid #ccc; /* Gray border */
          border-radius: 4px; /* Rounded borders */
          box-sizing: border-box; /* Make sure that padding and width stays in place */
          margin-top: 6px; /* Add a top margin */
          margin-bottom: 16px; /* Bottom margin */
          resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
        }

        /* Style the submit button with a specific background color etc */
        button[type=submit] {
          background-color: #04AA6D;
          color: white;
          padding: 12px 20px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
        }

        /* When moving the mouse over the submit button, add a darker green color */
        button[type=submit]:hover {
          background-color: #45a049;
        }

        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>

        <form action="https://formsubmit.co/alchemist999.c@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <label for="name">Your Name:</label><br>
             <input type="text" id="name" name="name" required><br>
             <label for="email">Your Email:</label><br>
             <input type="email" id="email" name="email" required><br>
             <label for="message">Your Message:</label><br>
             <!-- Adjust the cols attribute to change the width -->
             <textarea id="message" name="message" cols="50" required></textarea><br>
             <button type="submit">Submit</button>
        </form>"""
        st.markdown(contact_form, unsafe_allow_html=True)
