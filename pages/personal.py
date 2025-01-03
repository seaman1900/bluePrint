import streamlit as st
from blocks.auth import login, register
from blocks.dashboard import dashboard
import json
def app():
    if "is_login" not in st.session_state:
        # 为了测试方便，先设置为True
        st.session_state.is_login = True
    if st.session_state.is_login:
        with open('example_user_info.json', 'r', encoding='utf-8') as file:
            user_info = json.load(file)
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