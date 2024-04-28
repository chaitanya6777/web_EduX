import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDvrkAa65rqDrH0l1NcgYQTK7SRnH6wHj8")

# Set up the model and generation config
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

# Streamlit app
def app():
    st.title(":orange[AI] Chatbot :robot_face:")

    # Input question from user
    user_question = st.text_input("Ask a question:")

    # Initialize conversation
    convo = model.start_chat(history=[])

    # Process user input and display response
    if st.button("Send"):
        if user_question:
            try:
                # Send user's question to the model
                response = convo.send_message(user_question)
                st.write("Bot:", response.text)
            except genai.exceptions.StopCandidateException as e:
                st.error("Conversation ended. Please start a new conversation.")
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    app()
