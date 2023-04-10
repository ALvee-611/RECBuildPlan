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
