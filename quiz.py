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
    selected_indices = random.sample(range(len(questions)), num_questions)
    selected_questions = [questions[i] for i in selected_indices]
    selected_answers = [answers[i] for i in selected_indices]
    return selected_questions, selected_answers

def display_question(question):
    st.write("Question: " + question)

def app():
    st.title("Quiz Time!")
    st.write("Welcome to the Quiz.")
    
    file_path = "demo.txt"
    all_questions, all_answers = read_questions(file_path)
 
    if "selected_questions" not in st.session_state:
        num_questions = 2
        selected_questions, selected_answers = select_fixed_questions(all_questions, all_answers, num_questions)
        st.session_state.selected_questions = selected_questions
        st.session_state.selected_answers = selected_answers

    total_score = 0
    submitted = False
    user_answers = [""] * len(st.session_state.selected_questions)

    for index, question in enumerate(st.session_state.selected_questions):
        display_question(question)
        answer = st.text_input("Your Answer for Question {}: ".format(index + 1), value=user_answers[index])
        user_answers[index] = answer

    if st.button("Submit"):
        submitted = True
        for i, ans in enumerate(st.session_state.selected_answers):
            if user_answers[i].strip().lower() == ans.lower():
                total_score += 4
            else:
                total_score -= 1
        st.write("Total Score:", total_score)

if __name__ == "__main__":
    app()
