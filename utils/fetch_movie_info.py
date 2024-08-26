import requests


access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzg0Yzg2YmJmN2YxNDM0NGE4ZmIyZjBhZmExMGYwOCIsIm5iZiI6MTcyMzcyNjc3Mi4wMTc0NTQsInN1YiI6IjY2YmRlZjE4ZDQ2NGIyYTA3MDk3OTUxNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.0WWDHj0cXoMk0IKO8xko4u1ypgwyGja9Z5UN4WGgnrI'

# Setting up the headers with the access token (if required)
headers = {
    'Authorization': f'Bearer {access_token}'
}

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(url, timeout=5, headers=headers)
    if response.status_code == 200:
        poster_path = response.json().get('poster_path')
        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return full_path
        return None
    return None