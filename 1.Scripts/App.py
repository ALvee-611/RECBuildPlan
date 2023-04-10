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

unique_groups = get_data()['index_group_name'].unique()

department_name = unique_groups
# total items to display
total_items = 5
img_links = ["https://static.streamlit.io/examples/cat.jpg"]*total_items

for i in department_name:
    key_un = 'unique' + ' ' + str(i)
    c = create_comp(i,total_items, img_links, key_unique = key_un)

    st.title(c)


from st_click_detector import click_detector

clicked = clickable_images(img_links,
                            titles=[f"Image #{str(i)}" for i in range(5)],
                            div_style={"display": "flex", "flex-wrap": "wrap"},
                            img_style={"margin": "5px", "height": "500px"})


# if "my_inputs" not in st.session_state:
#         st.session_state["my_inputs"] = ""

# increment = click_detector(clicked)

#st.session_state["my_inputs"] = increment

if st.session_state["my_inputs"] == "Baby/Children1":
     st.write("This is inside the container")

# # Reads
# st.title(st.session_state["my_inputs"])

st.title("Products By Department")