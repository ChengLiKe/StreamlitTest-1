import random
import time

import streamlit as st

from menu import menu_with_redirect

menu_with_redirect()

if "messages" not in st.session_state:
    st.session_state.messages = []


def stream_data(words):
    message_placeholder = st.empty()
    full_response = ""
    for word in words:
        full_response += word + " "
        time.sleep(0.02)
        message_placeholder.markdown(full_response + "| ")


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    # 打印输入
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    # 打印输出（回复）
    with st.chat_message('assistant'):
        assistant_response = random.choice(
            [
                "傻逼",
                "滚",
                "典", "急", "崩", "麻", "笑"
            ]
        )
        stream_data(assistant_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_response}
    )
