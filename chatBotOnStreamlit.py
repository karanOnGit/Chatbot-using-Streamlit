import os
import time as t
from time import gmtime, strftime
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# dotenv_path = find_dotenv()
load_dotenv()
# api_key = os.environ["GOOGLE_API_KEY"]
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(history=[])


def greetings():
    greet = t.localtime()
    current_time = t.gmtime()

    day = strftime("%a", gmtime())
    date = current_time.tm_mday
    hour = greet.tm_hour
    # st.header(day)

    if 6 <= hour <= 12:
        st.header(f":red[{day} {date}], Good Morning! Karan")
    elif 13 <= hour <= 18:
        st.header(f":red[{day} {date}], Good Afternoon! Karan")
    elif 19 <= hour <= 24:
        st.header(f":red[{day} {date}], Good Evening! Karan")


def get_gemini_response(question):
    response = genai.chat(messages=question)
    return response.last


def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


if __name__ == "__main__":
    greetings()

    # Sending my message to chatBot and get the response
    user_prompt = st.chat_input("Asking...")
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # Displaying response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

    # if input:
    #     response = get_gemini_response(input)
    #     st.session_state["chat_history"].append((":black[You]", input))
    #     st.subheader(":robot_face: Bot reply: ", divider="rainbow")
    #     st.write(response)
    #     st.session_state["chat_history"].append((":black[Bot reply]", response))
