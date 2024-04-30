import streamlit as st
import random

def read_questions(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    questions = []
    answers = []
    for i in range(0, len(lines), 2):
        questions.append(lines[i].strip())
        answers.append(lines[i+1].strip())
    return questions, answers

def select_fixed_questions(questions, answers, num_questions):
    # Selecting a fixed number of questions from the given lists
    selected_indices = random.sample(range(len(questions)), num_questions)
    selected_questions = [questions[i] for i in selected_indices]
    selected_answers = [answers[i] for i in selected_indices]
    return selected_questions, selected_answers

def display_question(question):
    st.write("Question: " + question)

def app():
    st.title("Quiz Time!")
    st.write("Welcome to the Quiz.")
    
    # Specify the file path here
    file_path = "demo.txt"
    all_questions, all_answers = read_questions(file_path)
    
    # Check if the quiz has started
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    
    # Check if the quiz has ended
    if "quiz_ended" not in st.session_state:
        st.session_state.quiz_ended = False
    
    # Start quiz if it hasn't started yet
    if not st.session_state.quiz_started:
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
    
    # Hide the "Start Quiz" button once the quiz starts
    if st.session_state.quiz_started and not st.session_state.quiz_ended:
        # Hide the "Start Quiz" button
        st.session_state.quiz_started = True
        
        # Check if questions have been selected before
        if "selected_questions" not in st.session_state or st.session_state.selected_questions is None:
            # Select 2 random questions
            num_questions = 2
            selected_questions, selected_answers = select_fixed_questions(all_questions, all_answers, num_questions)
            st.session_state.selected_questions = selected_questions
            st.session_state.selected_answers = selected_answers
        
        total_score = 0
        submitted = False
        
        if st.session_state.selected_questions is not None:
            user_answers = [""] * len(st.session_state.selected_questions)
        else:
            user_answers = []
            
        for index, question in enumerate(st.session_state.selected_questions):
            display_question(question)
            
            # Check if user has already answered this question
            answer = st.text_input("Your Answer for Question {}: ".format(index + 1), value=user_answers[index] if user_answers else "")
            if user_answers:
                user_answers[index] = answer
            
        # Display submit button after all questions
        if st.button("Submit"):
            submitted = True
            for i, ans in enumerate(st.session_state.selected_answers):
                if user_answers[i].strip().lower() == ans.lower():
                    total_score += 4
                else:
                    total_score -= 1
            st.write("Total Score:", total_score)
            st.session_state.quiz_ended = True
    
    # Reset quiz state after submission
    if st.session_state.quiz_ended:
        st.session_state.quiz_started = False
        st.session_state.quiz_ended = False
        st.session_state.selected_questions = None
        st.session_state.selected_answers = None

if __name__ == "__main__":
    app()
