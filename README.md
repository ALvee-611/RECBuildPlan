For this challenge you are given the purchase history of customers across time, along with supporting metadata. Your challenge is to predict what articles each customer will purchase in the 7-day period immediately after the training data ends. Customer who did not make any purchase during that time are excluded from the scoring.
Files

    images/ - a folder of images corresponding to each article_id; images are placed in subfolders starting with the first three digits of the article_id; note, not all article_id values have a corresponding image.
    articles.csv - detailed metadata for each article_id available for purchase
    customers.csv - metadata for each customer_id in dataset
    sample_submission.csv - a sample submission file in the correct format
    transactions_train.csv - the training data, consisting of the purchases each customer for each date, as well as additional information. Duplicate rows correspond to multiple purchases of the same item. Your task is to predict the article_ids each customer will purchase during the 7-day period immediately after the training data period.

NOTE: You must make predictions for all customer_id values found in the sample submission. All customers who made purchases during the test period are scored, regardless of whether they had purchase history in the training data

# Customer Activity Analysis and Recommender System Planning

This project is organized in a modular structure, following the principles of software engineering best practices. The code is written in Python and the repository is structured as follows:

```
project
│   README.md
│   requirements.txt
│
└───1.Scripts
│   │   main.py
│   │   module1.py
│   │   module2.py
│   │   ...
│   
└───2. Notebooks
│   │   data.csv
|   |   
|   └───Building Recommender
|       │   file.ipynb
│   │   ...
│   
└───4.Insights
│   │   report.pdf
│   │   ...
│   
└───tests
│   │   test_module1.py
│   │   test_module2.py
│   │   ...

```

## Project Structure

- `src`: This folder contains the source code of the project, which includes Python scripts, modules, and packages.
- `data`: This folder contains data files used by the project.
- `docs`: This folder contains project documentation such as reports, user manuals, and design documents.
- `tests`: This folder contains the unit tests for the project.

## File Descriptions

- `README.md`: This file contains a brief introduction and overview of the project.
- `requirements.txt`: This file contains the required packages and dependencies for running the project.
- `main.py`: This file is the entry point of the project and contains the main function to run the code.
- `module1.py`: This file contains the code related to the module1 of the project.
- `module2.py`: This file contains the code related to the module2 of the project.
- `data.csv`: This file contains the raw data used by the project.
- `report.pdf`: This file contains the project report and documentation.
- `test_module1.py`: This file contains the unit tests for module1.
- `test_module2.py`: This file contains the unit tests for module2.

## Conclusion

This is a basic project structure that can be used as a template for organizing projects of different sizes and complexity. It provides a clear separation of concerns, easy maintenance, and scalability.