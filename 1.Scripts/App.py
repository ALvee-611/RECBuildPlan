import streamlit as st
import pandas as pd
import numpy as np

from st_clickable_images import clickable_images

from utils_funcs import *

@st.cache_data
def get_data():
    data = pd.read_csv('ranked_result.csv')
    return data


st.sidebar.subheader("Next Page")


st.title("Products By Department")

st.write("---")

##TEST##
placeholder = st.empty()
# Another session
if "department_input" not in st.session_state:
    st.session_state["department_input"] = ""
#############

unique_groups = get_data()['index_group_name'].unique()

department_name = unique_groups
# total items to display
total_items = 5
img_links = ["https://static.streamlit.io/examples/cat.jpg"]*total_items

if st.session_state["department_input"] == "":
    with placeholder.container():
        for i in department_name:
            key_un = 'unique' + ' ' + str(i)
            c = create_comp(i,total_items, img_links, key_unique = key_un)
else:
    placeholder.empty()
    with placeholder.container():
        submit = st.button("Submit")
        if submit:
            st.session_state["department_input"] = "A" 
            if st.session_state["department_input"] == "A":
                with st.container():
                    for i in department_name:
                        key_un = 'unique' + ' ' + str(i)
                        c = create_comp(i,total_items, img_links, key_unique = key_un)
                    placeholder.empty()



import streamlit as st
from st_click_detector import click_detector

content = """<p><a href='#' id='Link 1'>First link</a></p>
    <p><a href='#' id='Link 2'>Second link</a></p>
    <a href='#' id='Image 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
    <a href='#' id='Image 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    """
clicked = click_detector(content, key = "under")

st.markdown(f"**{clicked} clicked**" if clicked != "" else "**No click**")


def display_data(data):
    st.write(data)

if "n" not in st.session_state:
        st.session_state["n"] = ""

def ran(n):
    if n == 1:
        st.session_state["n"] = 0
        return ['https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'] * 3
    else:
        st.session_state["n"] = 1
        return ['https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200']*3


clicker = clickable_images(['https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200']*3,
                            titles=[f"Image #{str(i)}" for i in range(3)],
                            div_style={"display": "flex", "flex-wrap": "wrap"},
                            img_style={"margin": "5px", "height": "500px"}, key = "key_unique")

st.write("Outside Click", st.session_state["n"])

if clicker == 2:
    if st.session_state["n"] == "":
        st.session_state["n"] = 1

    result = ran(st.session_state["n"])
    st.write(result)
    st.image(result[0])
    st.write("Inside Click", st.session_state["n"])