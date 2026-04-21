import pandas as pd
import pickle
import requests

# load data
new_df = pickle.load(open('data/movie_list.pkl', 'rb'))
similarity = pickle.load(open('data/similarity.pkl', 'rb'))

# fetch poster
def fetch_poster(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey=716e01d9"
    data = requests.get(url).json()

    if data.get('Response') == 'True':
        return data.get('Poster')
    else:
        return "https://via.placeholder.com/200x300?text=No+Image"

# recommendation
def recommend(movie):
    if movie not in new_df['title'].values:
        return [{
            "title": "Movie not found. Please try another name.",
            "poster": "",
            "rating": "",
            "genres": ""
        }]

    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x: x[1])[1:6]

    results = []

    for i in movies_list:
        row = new_df.iloc[i[0]]

        results.append({
            "title": row.title,
            "poster": fetch_poster(row.title),
            "rating": round(row.vote_average, 1),
            "genres": ", ".join(row.genres)
        })

    return results