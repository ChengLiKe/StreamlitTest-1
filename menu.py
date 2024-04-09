import streamlit as st


def authenticated_menu():
    # 为已登录用户显示一个菜单
    st.sidebar.page_link("app.py", label="切换账户")
    st.sidebar.page_link("pages/user.py", label="个人信息")
    st.sidebar.page_link("pages/ResourceManage.py", label="资源管理")
    st.sidebar.page_link("pages/ServiceManage.py", label="服务管理")
    st.sidebar.page_link("pages/test.py", label="测试界面")
    if st.session_state.role in ["管理员", "超级管理员"]:
        st.sidebar.page_link("pages/admin.py", label="管理员")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="超级管理员",
            disabled=st.session_state.role != "超级管理员",
        )
    # st.switch_page("pages/welcome.py")

def unauthenticated_menu():
    # 为未登录用户显示一个菜单
    # st.sidebar.page_link("app.py", label="登录")
    pass


def menu():
    # 判断用户是否已登录，呈现不同菜单
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # 检查用户是否已登录，然后将其重定向到主页或呈现菜单
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()
