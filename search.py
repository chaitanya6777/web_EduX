# search.py

import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to search topics using Wikipedia API
def search_wikipedia(query):
    url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('query', {}).get('search', [])
    else:
        return []

def app():
    st.header("Topic Search")
    query = st.text_input("Enter topic:", "")
    if st.button("Search"):
        if query:
            results = search_wikipedia(query)
            if results:
                st.write("### Search Results:")
                for item in results:
                    title = item.get('title', 'No Title')
                    summary = item.get('snippet', 'No Summary')
                    soup = BeautifulSoup(summary, 'html.parser')
                    cleaned_summary = soup.get_text()
                    page_url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
                    st.write(f"**Title:** [{title}]({page_url})")
                    st.write(f"**Summary:** {cleaned_summary}")
                    st.write("---")
            else:
                st.write("No results found.")
