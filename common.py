import streamlit as st


def init():
    _page_config()
    _horizontal_radio_button()
    _remove_hamburger_menu()


def _horizontal_radio_button():
    # Horizontal Radio Button
    # https://discuss.streamlit.io/t/horizontal-radio-buttons/2114/3
    st.write(
        '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


def _page_config():
    st.set_page_config(
        page_title='부동산 연구소', page_icon=':house:', layout='wide')


def _remove_hamburger_menu():
    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
