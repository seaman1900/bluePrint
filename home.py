# 首页
import streamlit as st

# 初始化sessions_state, 方便后面写的时候位置不会混乱
def init_states():
    pass


if __name__ == "__main__":
    st.session_state.page = "home"
    if st.session_state.get("page")=="home":
        st.set_page_config(layout="wide")
    st.title("Welcome to BluePrint")
    # 居中显示
    st.markdown("<h1 style='text-align: center;'>Make Everything Valuable</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>article, image, video, code...</p>", unsafe_allow_html=True)

    # 当前状态展示

    st.subheader("what is bluePrint?")
    st.caption("在bluePrint分享您的优质内容, 获得多元化的收益, 弥补开源之殇的一块拼图")
    st.subheader("内容变现")
    st.caption("发布Print, 它将是您最直接的收入来源")  # 后续可以引进佣金系统，推广的人可以分得一部分
    st.subheader("版权保护")
    st.caption("转载收费, 保护原创")
    st.subheader("社区自治")
    st.caption("用户自治, 驱逐低质内容, 删除引战言论")
    st.subheader("多样投资")
    st.caption("投资您喜欢的Print, 获得收益分红") # 投资方式多元化，直接对口
