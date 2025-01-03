# 展示数据
import streamlit as st

def title(text):
    col1, col2 = st.columns([2,4])
    col1.markdown('<h4>'+text+'</h4>',unsafe_allow_html=True)
    col2.divider()

def dashboard(user_info):
    col1, col2 = st.columns([2,4])

    with col1:
        st.image(user_info['avatar_url'], width=100)
        st.subheader(user_info['username'])
        st.caption(user_info['profile']['description'])
        st.divider()

        st.subheader('待补充')
        st.caption('follower:100k')
        st.caption('likes:100k')
        st.caption('dislikes:100k')
    with col2:
        st.markdown('<h3>'+user_info['profile']['bio']+'</h3>', unsafe_allow_html=True)
        st.divider()
        title("Data Preview")
        # 展示数据
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.container(border=True):
                st.metric('作品数量', 100)
        with col2:
            with st.container(border=True):
                st.metric('获赞', 1000)
        with col3:
            with st.container(border=True):
                st.metric('总收益', 1000)

        title("作品清单")
        st.markdown('***作品1*** 获赞: 10k 获踩: 1k 收益: 10k')
        st.markdown('***作品2*** 获赞: 10k 获踩: 1k 收益: 10k')
        st.markdown('***作品3*** 获赞: 10k 获踩: 1k 收益: 10k')

        title("收藏内容")
        st.markdown('***作品1*** 获赞: 10k 获踩: 1k 收益: 10k')
        st.markdown('***作品2*** 获赞: 10k 获踩: 1k 收益: 10k')
        st.markdown('***作品3*** 获赞: 10k 获踩: 1k 收益: 10k')
