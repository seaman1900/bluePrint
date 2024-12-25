import streamlit as st

def head(content_info):
    col1, col2, col3 = st.columns([1,4,1], vertical_alignment='center', gap='medium')
    col1.image('https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg')
    with col2:
        col2.html('<h3>'+ content_info['title'] +'</h3>')
        st.caption("📅 "+ content_info['date'] +" by " + content_info['author'])
    with col3:
        # 价格
        st.markdown(":green-background[$"+ content_info['price'] +"]")

def main_content(content_info):
    st.write(content_info['description'])
    

# 状态信息显示
def status_bar(content_info):
    col1, col2, col3, col4, col5 = st.columns(5, vertical_alignment='center')
    col1.caption("👀 " + content_info['status']['view'])
    col2.caption("💬 " + content_info['status']['comment'])
    col3.caption("👍 " + content_info['status']['like'])
    col4.caption("👎 " + content_info['status']['dislike'])
    st.session_state.current_content_key = content_info['content_key']
    if content_info['buy_state'] == 'unpaid':
        if col5.button("preview", key=content_info['preview_key']):
            preview(content_info)
    elif content_info['buy_state'] == 'paid':
        if col5.button("detail", key=content_info['preview_key']):
            st.session_state.view_type = "detail"
            st.rerun()
    elif content_info['buy_state'] == 'free':
        if col5.button("free", key=content_info['preview_key']):
            st.session_state.view_type = "detail"
            st.rerun()

# 资金相关
def show_money():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        with st.popover("🔥 100"):
            st.write("推荐人数： 100")
    with col2:
        with st.popover("💴 10k"):
            st.write("赞助商： Nike Timmy...")
    with col3:
        with st.popover("🔧 10k"):
            st.write("参与维护人数： 1000")
    with col4:
        with st.popover("📈 100k"):
            # 收益曲线
            st.write("总收益： 100k")
# 预览界面
@st.dialog("Preview")
def preview(content_info):
    st.write("这是预览界面")
    if st.button("buy", key=content_info['content_key']):
        st.session_state.view_type = "detail"
        st.rerun()

def single_print(content_info):
    with st.container(border=True):
        head(content_info)
        main_content(content_info)
        status_bar(content_info)
        show_money()