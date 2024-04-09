import random

import pandas as pd
import streamlit as st
from menu import menu_with_redirect


def upload_resource():
    pass


# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.markdown("##### 资源管理")
st.divider()

df = pd.DataFrame(
    [
        {"资源名称": "数学PDF资源", "资源数量": 546, "服务调用数量": 2},
        {"资源名称": "语文Word资源", "资源数量": 376, "服务调用数量": 3},
        {"资源名称": "英语PDF资源", "资源数量": 509, "服务调用数量": 1},
    ]
)

# 设置num_rows="dynamic"来允许用户添加和删除行。
edited_df = st.data_editor(
    df,
    num_rows="dynamic",
    width=1000
)
st.divider()

col1, col2 = st.columns(2)

if col1.button('资源上传'):
    upload_resource()

if col2.button('查看资源'):
    st.json(df.to_json(orient="records"))

st.divider()
