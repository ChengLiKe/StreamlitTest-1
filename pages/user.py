import json

import pandas as pd
import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

with open('UserData/user.json', 'r', encoding='utf') as f:
    data = json.load(f)
    _password = data[st.session_state.username]['password']
    _role = data[st.session_state.username]['role']
    st.markdown("##### 个人信息")
    st.divider()
    st.text(f'姓名：{st.session_state.username}')
    st.text(f'密码：{_password}')
    st.text(f'权限：{_role}')

