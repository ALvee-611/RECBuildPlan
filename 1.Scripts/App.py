import streamlit as st
from PIL import Image
import urllib.request

url = 'https://storage.googleapis.com/kagglesdsdata/datasets/42780/75676/natural_images/car/car_0001.jpg'
with urllib.request.urlopen(url) as url_response:
    img = Image.open(url_response)
    st.image(img, caption='Image from the internet')



'F:\\Notebooks\\recommedner\\Deployment\\results\\images\\0108775015.jpeg'