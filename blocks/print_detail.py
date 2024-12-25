# 详情页
import streamlit as st

# 评论区
def comments():
    
    pass

def print_detail(content_key):
    st.title("Hello World")
    if st.button("back", key="back", icon=':material/arrow_back:', type='tertiary'):
        st.session_state.view_type = 'preview'
        st.rerun()
    
    st.write(content_key)
    st.markdown("hello world fucking code")
