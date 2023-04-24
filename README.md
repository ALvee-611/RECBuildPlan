# Customer Activity Analysis and Recommender System Planning

This GitHub repository contains code for performing exploratory data analysis on Kaggle datasets and building a recommender system using Python and SQL. The repository includes detailed documentation and examples for both parts of the project.

```
project
│   README.md
│   requirements.txt
│
└───1.Scripts
│   │   app.py
│   │   helper.py
│   │   modify_images.py
│   
└───2. Notebooks
│   │   articles_EDA
│   │   customer_EDA
|   |   transactions_EDA
|   |   
|   └───Building Recommender
|       │   ContentBased_REC_SYS_V1.ipynb
|       |   Popularity_REC_SYS_V1
│   
└───4.Insights
│   │   README.md
│   
└───4. Data
│   │   mini_product_card.db
│   │   mini_production_processed.db
│   │   popularity_V2.db
|   |   product_description
│   
└───5. Assets
|   |   cat_pca_model.pkl
|   |   good_small_pca_model.pkl
|   |   merged_pca_model.pkl
|   |   name_pca_model.pkl

```

## Project Structure

- `1.Scripts`: This folder contains the source code of the project.
- `2. Notebooks`: This folder contains the Jupyter notebooks on EDA and reccomender model building.
- `3. Insights`: This folder contains project documentation.
- `4. Data`: This folder contains the data used by the project.
- `5. Assets`: This folder contains the PCA models used by this project

## File Descriptions

- `README.md`: This file contains a brief introduction and overview of the project.
- `requirements.txt`: This file contains the required packages and dependencies for the project.
- `app.py`: This file contains the main functions to run the code.
- `helper.py`: This file contains the helper  functions used by the app.
- `modify_images.py`: This file contains the code to downsize the images to load into GitHub.
- `articles_EDA.ipynb`: This file contains the detailed EDA on articles data.
- `customer_EDA.ipynb`: This file contains the detailed EDA on the customer data.
- `transactions_EDA.ipynb`: This file contains the detailed EDA on the transactions data.
- `ContentBased_REC_SYS_V1.ipynb`: This file contains the code and reasoning for implementing the content based recommender system.
- `Popularity_REC_SYS_V1.ipynb`: This file contains the code and reasoning for implementing the popularity based recommender system.

## Data Descriptions (Can be downloaded from [Kaggle](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data)):

- `images/` - a folder of images corresponding to each article_id; images are placed in subfolders starting with the first three digits of the article_id; note, not all article_id values have a corresponding image.
- `articles.csv` - detailed metadata for each article_id available for purchase
- `customers.csv` - metadata for each customer_id in dataset
- `sample_submission.csv` - a sample submission file in the correct format
- `transactions_train.csv` - the training data, consisting of the purchases each customer for each date, as well as additional information. Duplicate rows correspond to multiple purchases of the same item. Your task is to predict the article_ids each customer will purchase during the 7-day period immediately after the training data period.

## Conclusion

This project currently built a product recommendations based on item features and popularity with an otpion for users to get item recommendations based on the item description they input on a search bar.