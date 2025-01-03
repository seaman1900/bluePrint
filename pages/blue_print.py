import streamlit as st

from blocks.single_print import single_print
from blocks.print_detail import print_detail

content_info = {
    "avatar": "https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg",
    "title": "hello world",
    "author": "Rex",
    "date": "2022-12-12 12:00",
    "price": '0.1',
    "description": "hello world, fucking code",
    "main_content": "hello world, fucking code",
    "status": {
        "view": '100000',
        "comment": '224',
        "like": '1200',
        "dislike": '12'
    },
    'buy_state': 'paid', # paid / unpaid / free
    'content_key': "test_key1",
    "preview_key": "preview1",
}

content_info_2 = {
    "avatar": "https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg",
    "title": "hello world",
    "author": "Rex",
    "date": "2022-12-12 12:00",
    "price": '0.1',
    "description": "hello world, fucking code",
    "main_content": "hello world, fucking code",
    "status": {
        "view": '100000',
        "comment": '224',
        "like": '1200',
        "dislike": '12'
    },
    'buy_state': 'free', # paid / unpaid / free
    'content_key': "test_key2",
    "preview_key": "preview2",
}
content_info_3 = {
    "avatar": "https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg",
    "title": "hello world",
    "author": "Rex",
    "date": "2022-12-12 12:00",
    "price": '0.1',
    "description": "hello world, fucking code",
    "main_content": "hello world, fucking code",
    "status": {
        "view": '100000',
        "comment": '224',
        "like": '1200',
        "dislike": '12'
    },
    'buy_state': 'unpaid', # paid / unpaid / free
    'content_key': "test_key3",
    "preview_key": "preview3",
}

st.session_state.page = "blue_print"
if st.session_state.get("page") == "blue_print":
    st.set_page_config(layout='wide')

if 'view_type' not in st.session_state:
    st.session_state.view_type = 'preview'

if st.session_state.view_type == 'preview':
    st.title("Blue Print")
    col1, col2, col3 = st.columns(3)
    with col1:
        single_print(content_info)
    with col2:
        single_print(content_info_2)
    with col3:
        single_print(content_info_3)
else:
    if "current_content_key" in st.session_state:
        print_detail(st.session_state.current_content_key)
    else:
        st.write("error")
