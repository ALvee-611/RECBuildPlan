from flask import Flask, render_template
import pickle

ranked_data = pickle.load(open('ranked_results.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', articles = list(ranked_data['article_id'].values),
                           department = list(ranked_data['index_group_name'].values),
                           ranking = list(ranked_data['ranked'].values))


@app.route('/CF_item')
def recommend_item():
    return render_template('CF_item.html')

if __name__ == '__main__':
    app.run(debug=True)