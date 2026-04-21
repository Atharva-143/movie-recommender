from flask import Flask, render_template, request, jsonify
from model import recommend, new_df

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend')
def get_recommendation():
    movie = request.args.get('movie')
    movies = recommend(movie)
    return render_template('index.html', movies=movies)

@app.route('/movies')
def get_movies():
    return jsonify(list(new_df['title'].values))

if __name__ == '__main__':
    app.run(debug=True)