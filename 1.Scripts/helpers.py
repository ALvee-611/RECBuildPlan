import os
import pandas as pd
import configparser
import matplotlib.image as mpimg
from sqlalchemy import create_engine, text as sql_text

import seaborn as sns
import matplotlib.pyplot as plt

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



def detail_process(user_input):
    """
    Preprocess user input and reduce feature size
    """
    #Get embeddings for the sentences
    sentence_embeddings = model_nlp.encode(user_input).reshape(1, -1)
    # reduce number of features:
    # Load the PCA model from file
    with open('..\\..\\assets\\good_small_pca_model.pkl', 'rb') as f:
        pca = pickle.load(f)
    processed = pca.transform(sentence_embeddings)
    return processed