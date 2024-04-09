import json

import pandas as pd
import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["超级管理员"]:
    st.warning("你没有资格查看此页面.")
    st.stop()

st.markdown("##### 用户管理-超级管理员")
st.divider()

with open('UserData/user.json', 'r', encoding='utf') as f:
    data = json.load(f)
    user = []
    for key, value in data.items():
        item = {
            "名称": key,
            "密码": value['password'],
            "权限": value['role']
        }
        user.append(item)

df = pd.DataFrame(user)
edited_df = st.data_editor(
    df,
    num_rows="dynamic",
    width=1000
)
st.divider()
