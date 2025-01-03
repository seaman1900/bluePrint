# 这个版本可以使用其他账户登录，比较正式，先用一个简陋的版本代替

import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# stauth.Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)
tab1, tab2 = st.tabs(["Login", "Register"])
with tab1:
    # login module
    try:
        authenticator.login()
    except Exception as e:
        st.error(e)

    try:
        col1, col2 = st.columns(2, vertical_alignment='center')
        with col1:
            authenticator.experimental_guest_login('Login with Google',
                                            provider='google',
                                            oauth2=config['oauth2'])
        with col2:
            authenticator.experimental_guest_login('Login with Microsoft',
                                            provider='microsoft',
                                            oauth2=config['oauth2'])
    except Exception as e:
        st.error(e)
with tab2:
    # register module
    try:
        email_of_registered_user, \
        username_of_registered_user, \
        name_of_registered_user = authenticator.register_user(pre_authorized=config['pre-authorized']['emails'])
        if email_of_registered_user:
            st.success('User registered successfully')
    except Exception as e:
        st.error(e)

if st.session_state['authentication_status']:
    with open('./config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')