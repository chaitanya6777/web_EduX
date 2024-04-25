import streamlit as st
from streamlit_option_menu import option_menu

import home,search, contact,resources

st.set_page_config(page_title="EduX", page_icon="🇮🇳", layout="wide")

class Multiapp:
    
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({"title": title, "function": function})

def run():
    with st.sidebar:
        app = option_menu(
            menu_title='EduX',
            options=['Home','Search','Contact Us','Resources'], 
            icons=['house-fill','search', 'chat-fill','message','pushpin'],  
            menu_icon='chat-text-fill',
            default_index=1,
            styles={
                "container": {"padding": "5!important", "background-colour": 'black'},  
                "icon": {"colour": "white", "font-size": "23px"},  
                "nav-link": {"colour": "white", "font-size": "20px", "text-align": "left", "margin": "0px" ,"--hover-color": "blue"},  
                "nav-link-selected": {"background-colour": "#02ab21"}, 
            }
        )

    if app == 'Home':
        home.app()
    elif app == "Search":
        search.app()
    elif app == 'Contact Us':
        contact.app()
    elif app== "Resources":
        resources.app()
run()
