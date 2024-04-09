import random
import time

import streamlit as st
from openai import OpenAI

from menu import menu_with_redirect

menu_with_redirect()

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sk-OEnSWTWbvI9cfFK5cjLX4M3mDqIDC2i1OrbFrYmtYi25RtsV",
    base_url="https://api.chatanywhere.tech/v1"
)


def gpt_35_api(messages: list):
    """为提供的对话消息创建新的回答

    Args:
        messages (list): 完整的对话消息
    """
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    return completion.choices[0].message.content


def gpt_35_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
    """
    stream = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            time.sleep(0.02)
            print(chunk.choices[0].delta.content)


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
        # assistant_response = random.choice(
        #     [
        #         "傻逼",
        #         "滚",
        #         "典", "急", "崩", "麻", "笑"
        #     ]
        # )
        assistant_response = gpt_35_api(st.session_state.messages)
        stream_data(assistant_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_response}
    )
