# 登录 注册 忘记密码
import streamlit as st

def login():
    with st.form("login"):
        username = st.text_input("用户名")
        password = st.text_input("密码", type="password")
        submit_button = st.form_submit_button(label="登录")
        if submit_button:
            st.write("登录成功！")
            st.session_state["username"] = username
            st.session_state["password"] = password
            st.session_state["is_login"] = True
            st.rerun()

def register():
    with st.form("register"):
        username = st.text_input("用户名")
        password = st.text_input("密码", type="password")
        confirm_password = st.text_input("确认密码", type="password")
        submit_button = st.form_submit_button(label="注册")
        if submit_button:
            if password != confirm_password:
                st.error("密码不一致！")
            else:
                st.write("注册成功！")
                st.session_state["username"] = username
                st.session_state["password"] = password
                st.session_state["is_login"] = True
                st.rerun()