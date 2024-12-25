# # 单独的卡片界面设计
# import streamlit as st
# from blocks.preview import preview
# # info template
# config = {
#     'head': '这是标题',
#     'description': '这是简单介绍',
#     'image': './static/myxj.jpg'
# }

# stripe_publishable_key = 'pk_test_51QSrjDGfqDtvTF8ND1FhnKFbOiuwytMAiQqEoTlhfsQGXaF1JcKPZcHyKJ6pGUqvp4btSFPfOAcpkJnWPUSzFc6I00mYiucS2t'

# stripe_js = """	
#             <script async src="https://js.stripe.com/v3/buy-button.js"></script>	
#             <stripe-buy-button	
#             buy-button-id="buy_btn_1NKjSSBY7L5WREAJ0wKVXsQB"	
#             publishable-key="{}"
#             ></stripe-buy-button>	
#             """.format(stripe_publishable_key)

# def tags():
#     st.markdown(':blue-background[tag1] :red-background[tag2] :red-background[tag3] ')

# def seed_main(info):
#     col1, col2 = st.columns([8,4], vertical_alignment='top')
#     with col1:
#         st.header(info['head'])
#         st.caption(info['description'])
#     with col2:
#         st.image(info['image'])
# def seed_info(info):
#     col1, col2, col3, col4, col5, col6 = st.columns([4,4,4,4,4,4], vertical_alignment='center')
#     with col1:
#         st.caption("⏱ Nov 15, 2021")
#     with col2:
#         st.caption("💵 1,000")
#     with col3:
#         st.caption("💬 200")
#     with col4:
#         st.caption("👀 1,000")
#     with col5:
#         st.button("preview", use_container_width=True, key=info['key_preview_btn'], on_click=preview)
#     with col6:
#         if st.button("buy", use_container_width=True, key=info['key_buy_btn']):
#             st.session_state['view_state'] = 'detail'
#             st.rerun()
#         # st.html(stripe_js)
# def seed(info):
#     with st.container(border=True):
#         st.caption("🤠 written by rex jiang...")
#         seed_main(info)
#         tags()
#         seed_info(info)
