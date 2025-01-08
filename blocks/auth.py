# 登录 注册 忘记密码
import streamlit as st
import requests
import time

BASE_URL = "http://127.0.0.1:8000"

def login():
    with st.form("login"):
        username = st.text_input("用户名")
        password = st.text_input("密码", type="password")
        submit_button = st.form_submit_button(label="登录")
        if submit_button:
            url = f"{BASE_URL}/user/login"
            data = {
                "username": username,
                "password": password
            }
            response = requests.post(url, json=data)
            # 如果401 登录失败
            if response.status_code == 401:
                st.error("用户名或密码错误！")
            else:
                user_info = response.json().get("user_info")
                st.session_state["user_info"] = user_info
                st.session_state["is_login"] = True

                st.success(f"登录成功! 3s后跳转...")
                time.sleep(3)
                st.rerun()

def register():
    with st.form("register"):
        username = st.text_input("用户名")
        avatar_url = st.text_input("头像链接")
        email = st.text_input("邮箱")
        password = st.text_input("密码", type="password")
        confirm_password = st.text_input("确认密码", type="password")
        submit_button = st.form_submit_button(label="注册")
        if submit_button:
            if password != confirm_password:
                st.error("密码不一致！")
            else:
                url = f"{BASE_URL}/user/register"
                data = {
                    "username": username,
                    "email": email,
                    "avatar_url": avatar_url,
                    "password": password
                }
                response = requests.post(url, json=data)
                if response.status_code == 400:
                    st.error("注册失败！名字重复！")

                user_info = response.json().get("user_info")
                st.success(f"注册成功! 3s后跳转...")
                time.sleep(3)
                st.session_state["user_info"] = user_info
                st.session_state["is_login"] = True
                st.rerun()