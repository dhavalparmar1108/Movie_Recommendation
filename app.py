from flask import Flask, request, jsonify
import requests
import pickle
import gzip

app = Flask(__name__)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=2784c86bbf7f14344a8fb2f0afa10f08&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return full_path
    return None

new_data = pickle.load(open("movies_list.pkl", "rb"))

with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

movie_list = new_data['title'].values

def recommend(movie):
    if movie not in movie_list:
        return [], []  # Handle case where the movie is not found

    index = new_data[new_data['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    
    recommended_movies = []
    recommended_posters = []
    
    for i in distances[1:6]:  # Skip the first one because it is the movie itself
        movie_title = new_data.iloc[i[0]].title
        movie_id = new_data.iloc[i[0]].id
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

@app.route('/fetch-movies', methods=["GET"])
def fetch_movies():
    name = request.args.get('name')
    
    if not name:
        return jsonify({"error": "No movie name provided"}), 400

    recommended_movies, recommended_posters = recommend(name)

    if not recommended_movies:
        return jsonify({"error": "Movie not found"}), 404

    return jsonify({
        "recommended_movies": recommended_movies,
        "recommended_posters": recommended_posters
    })

if __name__ == '__main__':
    app.run(debug=True)

   
