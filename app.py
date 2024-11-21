import streamlit as st  # Correct import
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

# Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat!")

# Initialize ChatOpenAI model
chat = ChatOpenAI(temperature=0.5)

# Initialize session state for messages
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assistant.")
    ]

# Function to load OpenAI model and get response
def get_openai_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))  # Add user's message
    response = chat(st.session_state['flowmessages'])  # Get AI response
    st.session_state['flowmessages'].append(AIMessage(content=response.content))  # Add AI's response
    return response.content

# Input field for user message
user_input = st.text_input("Input: ", key="input")

# If user provides input, generate response
if user_input:
    response = get_openai_response(user_input)
    st.subheader("Response:")
    st.write(response)


   
    
   





