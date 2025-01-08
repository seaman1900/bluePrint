import streamlit as st
from blocks.auth import login, register
from blocks.dashboard import dashboard
from models.user import User

def app():
    if "is_login" not in st.session_state:
        # 为了测试方便，先设置为True
        st.session_state.is_login = False
    if st.session_state.is_login:
        user_dict = st.session_state.user_info
        user_info = User(**user_dict)
        dashboard(user_info)
    else:
        st.write("Please login or register to access your personal page.")
        tab1, tab2 = st.tabs(["Login", "Register"])
        with tab1:
            login()
        with tab2:
            register()

st.session_state.page = "personal"
if st.session_state.get("page") == "personal":
    st.set_page_config(layout='centered')
app()