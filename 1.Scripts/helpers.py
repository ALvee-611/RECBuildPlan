import os
import pandas as pd
import configparser
import matplotlib.image as mpimg
from sqlalchemy import create_engine, text as sql_text

import seaborn as sns
import matplotlib.pyplot as plt

import pickle

config = configparser.ConfigParser()
config.read('..\\..\\config.ini')

host = config['mysql']['host']
database = config['mysql']['database']
user = config['mysql']['user']
password = config['mysql']['password']
port = config['mysql']['port']

def read_query(query):
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
    df = pd.read_sql_query(sql = sql_text(query), con=engine.connect())
    print('Query Executed!')
    return df


def get_popular_item_rank(day_type):
    """
    get all items for each department ranked
    """
    if day_type == "weekday":
        q = """
        SELECT article_id, index_group_name, ranked
        FROM (
        SELECT article_id, index_group_name, day_type,
        RANK() OVER (PARTITION BY index_group_name,day_type ORDER BY total_purchases DESC) AS ranked
        FROM popularity_v1) R
        where day_type = "weekday";
        """
    else:
        q = """
        SELECT article_id, index_group_name, ranked
        FROM (
        SELECT article_id, index_group_name, day_type,
        RANK() OVER (PARTITION BY index_group_name,day_type ORDER BY total_purchases DESC) AS ranked
        FROM popularity_v1) R
        where day_type = "weekend";
        """

    return read_query(q)

#Test
get_popular_item_rank('weekend')



location_of_folder = "..//..//Processed_Images"

def dispaly_images(article_list,folder_location):
    """
        article_list is a list of all the ids of the articles we want to retrieve
    """
    for i in article_list:
        image_names = '0' + str(i) + '.jpg'
        image_location = os.path.join(folder_location, image_names)

        # Load the image from image location
        img = mpimg.imread(image_location)

        plt.imshow(img)
        plt.axis('off')
        plt.show()


def detail_process(user_input, model_nlp, pca_model_path,pca_model_name):
    """
    Preprocess user input and reduce feature size
    """
    # Locating the pca model location
    pca_loc = os.path.join(pca_model_path, pca_model_name)
    
    #Get embeddings for the sentences
    sentence_embeddings = model_nlp.encode(user_input).reshape(1, -1)
    
    # reduce number of features:
    with open(pca_loc, 'rb') as f:
        pca = pickle.load(f)
    processed = pca.transform(sentence_embeddings)
    
    return processed


## Finding the similar items based on item features:
from sklearn.neighbors import NearestNeighbors
import numpy as np

def similar_items(full_df, article_id, num_items = 6):
    """
    takes the dataframe full_df containing the articl_id and all the features and the articl_id of the
    items for which we need similar items, and then return list indices of the num_items(default 5) most similar items
    similar_items: DataFrame Int Int -> Listof(Int)
    """
    # get item index
    item_index = full_df[full_df['article_id'] == article_id].index[0]
    # saving the ids
    id_df = full_df['article_id']
    # dropping the article_id feature
    main_df = full_df.drop(columns=['article_id'], axis=1)

    item_A = np.array(main_df.iloc[item_index]).reshape(1, -1)

    # NearestNeighbors model(taking 6 since first item will be the item itself)
    nbrs = NearestNeighbors(n_neighbors=num_items, algorithm='auto').fit(main_df)

    # get distances and indices of nearest neighbors
    _, indices = nbrs.kneighbors(item_A)

    # the article_id of 5 most similar items
    id = list(id_df[indices[0]])

    return id

#example_id = 145872053
#similar_items(rest_df, example_id)