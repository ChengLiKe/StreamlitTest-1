import json

import streamlit as st
from menu import menu

# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None
if 'username' not in st.session_state:
    st.session_state.username = None
if 'password' not in st.session_state:
    st.session_state.password = None


def log_in(_username: str, _password: str):
    st.divider()
    with open('UserData/user.json', 'r', encoding='utf') as f:
        data = json.load(f)
        try:
            if data[_username]:
                print(f'用户{_username}存在')
                if data[_username]['password'] == _password:
                    print('密码正确')
                    # 持久化存储用户信息
                    st.session_state.role = data[_username]['role']
                    st.session_state.username = _username
                    st.session_state.password = _password
                    st.success('登录成功!', icon="✅")
                    st.title(f"欢迎来到教学资源推荐服务管理平台, {st.session_state.role}")
                else:
                    print('密码错误')
                    st.error('密码错误', icon="🚨")
                    st.session_state.role = None
        except KeyError:
            if _username == "":
                st.error('请输入账户')
            elif _password == "":
                st.error('请输入密码')
            else:
                print(f'用户{_username}不存在')
                st.error('用户未注册', icon="🚨")


username = st.text_input(
    label="输入账号",
    placeholder=st.session_state.username,
    label_visibility="collapsed"
)
password = st.text_input(
    label="<PASSWORD>",
    placeholder=st.session_state.password,
    label_visibility="collapsed"
)
if st.button(label="登录"):
    log_in(username, password)
menu()  # Render the dynamic menu!
