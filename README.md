# Movie Recommendation System API

This project is a Flask-based API that provides movie recommendations and suggestions based on a trained machine learning model. It fetches similar movies, along with posters, overviews, genres, and more, using data from The Movie Database (TMDB).

## Features

- Fetch Similar Movies: Get a list of movies similar to a given movie, along with posters, overviews, genres, and movie IDs.
- Movie Suggestions: Get movie name suggestions based on the input provided.

## Prerequisites

- Python 3.x
- Flask
- Requests
- Numpy
- Pickle
- Gzip

## Installation

1. Clone the repository

    ```bash
    git clone https://github.com/yourusername/movies-recommendation-api.git
    cd movies-recommendation-api

2. Install Dependencies:

    ```bash
    pip install -r requirements.txt

3. Prepare the Data Files:
    Ensure you have the following files in your project directory:
    
    - `movies_list.pkl` - Contains the movie data
    - `similarity.pkl.gz` - Contains the similarity matrix for movie recommendations.

4. Run the API:
    ```bash
    python app.py
    ```
    This command will start the server on your local machine.

## API Endpoints        

1. Fetch Similar Movies

    Endpoint: `/fetch-movies`

    Method: `GET`

    Parameters:

    - name: The name of the movie for which you want to fetch similar movies.

2. Response:

    - `recommended_movies`: List of recommended movie titles.
    - `recommended_posters`: List of URLs to the movie posters.
    - `recommended_overview`: List of overviews of the recommended movies.
    - `recommended_genre`: List of genres of the recommended movies.
    - `recommended_id`: List of TMDB IDs of the recommended movies.

    Example:
    ```bash
    curl "http://0.0.0.0:5000/fetch-movies?name=Inception"
    ```

    Response Example:
    ```json
    {
    "status": 200,
    "recommended_movies": ["Movie1", "Movie2", "Movie3"],
    "recommended_posters": ["url_to_poster1", "url_to_poster2", "url_to_poster3"],
    "recommended_overview": ["Overview1", "Overview2", "Overview3"],
    "recommended_genre": ["Genre1", "Genre2", "Genre3"],
    "recommended_id": [123, 456, 789]
    }

## Project Structure
    movies-recommendation-api/
    │
    ├── app.py                   # Main Flask application
    ├── movies_list.pkl          # Pickle file containing the movie data
    ├── similarity.pkl.gz        # Gzip file containing the similarity matrix
    ├── requirements.txt         # Project dependencies
    └── README.md                # This README file    

## How it Works
1. `Movie Data`: The project uses a pre-processed pickle file (movies_list.pkl) containing movie details and a similarity matrix (similarity.pkl.gz) to find similar movies.

2. `TMDB API`: The TMDB API is used to fetch additional movie details like posters using the movie IDs.

3. `Recommendation Logic`: The similarity matrix is used to find the top 15 most similar movies to the queried movie. The first result (the movie itself) is skipped.