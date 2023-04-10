import streamlit as st
import pandas as pd
import numpy as np

from st_clickable_images import clickable_images
from st_click_detector import click_detector


def create_comp(department_name,total_items,image_links, key_unique):
    st.header(department_name + ':')
    st.subheader("Most Popular items:")

    # Create the columns
    cols = st.columns(total_items)
    image_links

    clicked = clickable_images(image_links,
                            titles=[f"Image #{str(i)}" for i in range(5)],
                            div_style={"display": "flex", "flex-wrap": "wrap"},
                            img_style={"margin": "5px", "height": "500px"}, key = key_unique)
    

    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

###################################TEST#######################
    # # Another session
    # if "department_input" not in st.session_state:
    #     st.session_state["department_input"] = ""

    depart_input = department_name + str(clicked)

    
    st.session_state["department_input"] = depart_input

###############################################################

    st.write("---")