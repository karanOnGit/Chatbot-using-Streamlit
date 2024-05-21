import os

import time as t
from time import gmtime, strftime
import streamlit as st
import google.generativeai as genai
from dotenv import find_dotenv, load_dotenv, dotenv_values

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
api_key = os.environ["GOOGLE_API_KEY"]

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def greetings():
    greet = t.localtime()
    current_time = t.gmtime()

    day = strftime("%a", gmtime())
    date = current_time.tm_mday
    hour = greet.tm_hour

    if 12 <= hour <= 18:
        st.header(f":red[{day} {date}], Good Afternoon Karan")
    elif 19 <= hour <= 23:
        st.header(f":red[{day} {date}], Good Evening Karan")
    else:
        st.header(f":red[{day} {date}], Good Morning Karan")

def get_gemini_response(question):
    response = genai.chat(messages=question)
    return response.last


if __name__ == '__main__':
    greetings()

    input = st.text_input(":boy: You: ")
    # submit = st.button(":green[Ask]")

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    if input:
        response = get_gemini_response(input)
        st.session_state["chat_history"].append((":black[You]", input))
        st.subheader(":robot_face: Bot reply: ", divider="rainbow")
        st.write(response)
        st.session_state["chat_history"].append((":black[Bot reply]", response))

    # st.subheader("Chat History", divider="grey")
    st.sidebar.header(":blue[Chat History]", divider="grey")
    # st.sidebar.text("Your chats are saved here")
    
    for role, text in st.session_state["chat_history"]:
        st.sidebar.write(f"**{role}**:  {text}")
        st.sidebar.divider()
