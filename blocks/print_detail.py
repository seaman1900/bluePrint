# 详情页
import streamlit as st
import datetime

# 初始化评论列表
if 'comments' not in st.session_state:
    st.session_state.comments = [
        {
                "name": 'rex',  # 暂时先不写
                "auth_id": "001",
                "comment_id": "001",
                "comment": "this is a comment for you",
                "time": "2023-10-10 10:10:10",
                "avatar": "https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg"  # 默认头像
        },
        {
                "name": 'rex',  # 暂时先不写
                "auth_id": "001",
                "comment_id": "002",
                "comment": "this is a comment for you again",
                "time": "2023-10-10 10:20:10",
                "avatar": "https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg"  # 默认头像
        },
    ]

def single_comment(comment):
    col1, col2, col3 = st.columns([1,8,1], vertical_alignment='top')
    with col1:
        st.image(comment["avatar"], width=50)
    with col2:
        st.markdown("<h3>" + comment["name"] + "</h3>", unsafe_allow_html=True)
        st.caption(comment["time"])
        st.write(comment["comment"])
    with col3:
        st.button("回复", key=f"reply_{comment['comment_id']}", icon=':material/reply:', type='tertiary')
        

# 评论区
def comments(comments_info=None):
    with st.form("评论区"):
        user_comment = st.text_area("评论", placeholder="请友好交流", max_chars=250, key="comment_input")
        submit_button = st.form_submit_button("提交评论")
    # 提交评论
    if submit_button:
        if user_comment:
            # 获取当前时间
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 将评论添加到列表中
            st.session_state.comments.append({
                "name": 'rex',  # 暂时先不写
                "comment": user_comment,
                "time": current_time,
                "avatar": "https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg"  # 默认头像
            })
            st.success("评论已提交！")
        else:
            st.error("请填写名字和评论内容。")
    st.subheader("💬 所有评论")
    for idx, comment in enumerate(st.session_state.comments):
        single_comment(comment)
    st.button("load more")
# 资金池
def fund_pool():
    st.subheader("💰 资金池")
    st.markdown("当前资金池: :green-background[$100]")
    st.button("查看明细")

# 工作区
def workspace():
    # 用于记录为该内容做出贡献的人
    st.subheader("👥 贡献者")
    st.markdown("rex 于 2024-10-25 10:20:10 提交了法语翻译内容 获得了奖励: :green-background[$10]")

# 投资方式
def invest_bar():
    col1, col2, col3, col4 = st.columns(4)
    col1.button("购买热度")
    col2.button("购买翻译")
    col3.button("投放广告")
    col4.button("申请转载")

def print_detail(content_key):
    st.set_page_config("detail", layout="wide")
    
    empty, col1, col2 = st.columns([1,3,2], vertical_alignment='top')
    
    with col1:
        st.title("Hello World")
        if st.button("back", key="back", icon=':material/arrow_back:', type='tertiary'):
            st.session_state.view_type = 'preview'
            st.rerun()
        st.write(content_key)
        st.markdown("hello world fucking code")
        invest_bar()
        comments()
        
    with col2:
        st.header("📊 数据统计")
        workspace()
        fund_pool()