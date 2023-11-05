import random
import time

import streamlit as st
from streamlit_option_menu import option_menu

from configs import CONTENT_COL_CONFIG
from app_pages.home import show_home_page
from app_pages.function import show_function_page

# --- PAGE CONFIG AND NAV SESSION STATE---
st.set_page_config(page_title="Insightful Reviews", page_icon="⛳️", layout="wide")

if 'menu_option' not in st.session_state:
    st.session_state['menu_option'] = 'Home'

language = "en"

# https://github.com/victoryhb/streamlit-option-menu
# https://icons.getbootstrap.com/
menu_options = {
    "en": [
        {"label": "Home", "icon": "house"},
        {"label": "Try", "icon": "rocket"},
        {"label": "Price", "icon": "credit-card"},
    ], 
    "zh": [
        {"label": "主页", "icon": "house"},
        {"label": "体验", "icon": "rocket"},
        {"label": "定价", "icon": "credit-card"},
    ]
}

top_menu = option_menu(None, [option["label"] for option in menu_options[language]], 
                        icons=[option["icon"] for option in menu_options[language]], 
                        menu_icon="cast", default_index=0, orientation="horizontal", 
                        # styles={
                        #     "container": {"padding": "0!important", "background-color": "#fafafa"},
                        #     "icon": {"color": "orange", "font-size": "25px"}, 
                        #     "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                        #     "nav-link-selected": {"background-color": "grey"},
                        # }
                    )

# --- Page Footer ---
def show_page_footers():
    _, center, _ = st.columns(CONTENT_COL_CONFIG)

    with center:
        st.markdown("© 2023 Lightning Insights")


if top_menu in ("主页", "Home"): 
    show_home_page(language)

if top_menu in ("体验", "Try"): 
    show_function_page(language)

if top_menu in ("定价", "Price"): 
    show_pricing_page()

show_page_footers()
