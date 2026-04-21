import pandas as pd
import pickle
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv('data/tmdb_5000_movies.csv')
credits = pd.read_csv('data/tmdb_5000_credits.csv')

movies = movies.merge(credits, on='title')

# convert genres JSON → list
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)

# keep important columns
movies = movies[['movie_id','title','overview','genres','vote_average']]
movies.dropna(inplace=True)

# create tags
movies['tags'] = movies['overview']

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)

# save files
pickle.dump(movies, open('data/movie_list.pkl', 'wb'))
pickle.dump(similarity, open('data/similarity.pkl', 'wb'))

print("MODEL CREATED ✅")