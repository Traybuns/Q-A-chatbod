from langchain.llms import OpenAI  # Correctly import OpenAI

import streamlit as st

# Function to load OpenAI model and get responses
def get_openAI_response(question):
    llm = OpenAI(model_name="text-davinci-003", temperature=0.5)  # Correct variable name and parameter
    response = llm(question)
    return response

# Authenticate streaming app
st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

# Input field
user_input = st.text_input("Input:", key="input")

# Button for submission
submit = st.button("Ask the question")

# If submit button is clicked
if submit:
    if user_input:  # Check if user input is provided
        response = get_openAI_response(user_input)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.warning("Please enter a question!")
