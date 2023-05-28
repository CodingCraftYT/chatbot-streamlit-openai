# Import Libraries

import openai
import streamlit as st
from streamlit_chat import message

# Open API key

openai.api_key = st.secrets["OPEN_API_KEY"]

# Generating responses from the api

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    messages = completions.choices[0].text
    return messages

# Creating the chatbot interfaces

st.title("Chatbot : Coding Craft + OpenAI ")

# Storing the input

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# Creating a function that returns the user's input from a text input field

def get_text():
    input_text = st.text_input("You : ", "Hello, Coders, how are you?", key = "input")
    return input_text

# We will generate response using the 'generate response' function and store into variable called output

user_input = get_text()

if user_input:
    output = generate_response(user_input)

    # Store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


# Finally we display the chat history

if st.session_state['generated']:

    for i in range(len(st.session_state['generated']) -1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')










