# 首页
import streamlit as st

# 初始化sessions_state, 方便后面写的时候位置不会混乱
def init_states():
    pass


if __name__ == "__main__":
    st.title("Welcome to Farm👋")
    # 两个主要内容：付费平台、社区治理
    col1, col2 = st.columns(2)
    with col1:
        st.header("付费平台")
        st.write("付费平台")
    with col2:
        st.header("社区治理")
        st.write("社区治理")
