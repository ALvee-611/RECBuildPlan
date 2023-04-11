import streamlit as st
import os
from PIL import Image

import pickle
import numpy as np
from numpy.linalg import norm

import tensorflow as tf

from tensorflow.keras.layers import GlobalMaxPooling2D

from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input

feature_list = pickle.load(open('..\\2. Notebooks\\embeddings.pkl', 'rb'))

filenames = pickle.load(open('..\\2. Notebooks\\file_names_full.pkl', 'rb'))

if tf.test.gpu_device_name():
      print(f'Default GPU Device: {tf.test.gpu_device_name()}')

model = VGG16(weights='imagenet', include_top=False, input_shape = (224,224,3))
model.trainable = False

model_seq = tf.keras.Sequential([
      model,
      GlobalMaxPooling2D()])

from sklearn.neighbors import NearestNeighbors

st.title("Hey")

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('..\\1.Scripts\\Uploads', uploaded_file.name), 'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except:
        return 0
    

def feature_extraction(img_path, model):
    img_file = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img_file)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    predicted_output = model.predict(preprocessed_img)
    one_dim_output = predicted_output.flatten()
    output = one_dim_output/norm(one_dim_output)

    return output

def recommend(features, feature_list):
    neighbors = NearestNeighbors(n_neighbors = 5, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)
    distances, indices = neighbors.kneighbors([features])

    return indices


uploaded_file = st.file_uploader("Choose an image")

if uploaded_file is not 'None':
    if save_uploaded_file(uploaded_file):
        display_image = Image.open(uploaded_file)
        st.image(display_image)
        
        features = feature_extraction(os.path.join('..\\1.Scripts\\Uploads', uploaded_file.name), model_seq)

        indices = recommend(features, feature_list)

        #Show
        col1,col2,col3,col4,col5 = st.columns(5)

        with col1:
            location_img = os.path.join('..\\Test_all', filenames[indices[0][0]])
            st.image(location_img)
        with col2:
            location_img = os.path.join('..\\Test_all', filenames[indices[0][1]])
            st.image(location_img)
        with col3:
            location_img = os.path.join('..\\Test_all', filenames[indices[0][2]])
            st.image(location_img)
        with col4:
            location_img = os.path.join('..\\Test_all', filenames[indices[0][3]])
            st.image(location_img)
        with col5:
            location_img = os.path.join('..\\Test_all', filenames[indices[0][4]])
            st.image(location_img)

    else:
        st.write("Some Error occured")

