import streamlit as st

st.title("AI Startup Assistant")

st.write("This is a sample Gen AI project interface.")

business_name = st.text_input("Enter your startup or enterprise name")

user_problem = st.text_area("Describe the user problem")

user_question = st.text_area("Ask the chatbot a question")

if st.button("Generate Response"):
    st.write("Sample response will appear here.")
    st.write("Later, students can connect this app with an AI API.")
