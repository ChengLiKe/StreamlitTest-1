import random

import pandas as pd
import streamlit as st
from menu import menu_with_redirect


def upload_resource():
    pass


# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()
st.markdown("##### 服务管理")
st.divider()

df = pd.DataFrame(
    [
       {"服务名称": "服务1", "资源名称": "语文PDF资源", "调用模型": "Bert大模型"},
       {"服务名称": "服务2", "资源名称": "数学PDF资源", "调用模型": "CLIP多模态大模型"},
       {"服务名称": "服务3", "资源名称": "英语PDF资源", "调用模型": "Bert大模型"},
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

if col1.button('服务新增'):
    upload_resource()

if col2.button('查看服务'):
    st.json(df.to_json(orient="records"))

st.divider()
