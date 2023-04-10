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
    st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")

    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    increment = clicked

    my_input = department_name + str(clicked)

    key_un = 'unique' + ' ' + key_unique

    submit = st.button("Submit", key=key_un)

    if submit:
        st.session_state["my_input"] = my_input
        st.write("You entered ", my_input)

    if st.session_state["my_input"] == "Baby/Children1":
        with st.container():
            st.write("This is inside the container")

        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))
    else:
        st.empty()

    st.write("---")
    return increment