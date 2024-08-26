import pickle
import gzip
from utils import fetch_movie_info as movie_info
from logging_utils import logger

class Utility:
    def __init__(self):
        # Load the movie list
        self.new_data = pickle.load(open("movies_list.pkl", "rb"))
        self.logger = logger.Logger()
        # Load the similarity matrix
        with gzip.open('similarity.pkl.gz', 'rb') as f:
            self.similarity = pickle.load(f)

        # Convert the movie titles to lowercase
        self.movie_list = self.new_data['title'].values
        self.movie_list = [title.lower() for title in self.movie_list]

    def getSuggestion(self, movie):
        suggestions = self.new_data[self.new_data['title'].str.lower().startsWith(movie.lower())]
        suggestions = suggestions['title'].head(10)
        return suggestions.values.tolist()

    def recommend(self,movie):
        try:
            
            movie = movie.lower()
            movie = movie.strip()
            self.logger.log("movie is " + movie)
            
            recommendations = {
                'recommended_movies': [],
                'recommended_posters': [],
                'recommended_overview': [],
                'recommended_genre': [],
                'recommended_id':[]
            }

            if movie not in self.movie_list:
                return recommendations  # Handle case where the movie is not found

            index = self.new_data[self.new_data['title'].str.lower() == movie].index[0]
            distances = sorted(list(enumerate(self.similarity[index])), reverse=True, key=lambda vector: vector[1])
        
            for i in distances[1:6]:  # Skip the first one because it is the movie itself
                movie_title = self.new_data.iloc[i[0]].title
                overview = self.new_data.iloc[i[0]].overview
                genre = ""
                movie_id = self.new_data.iloc[i[0]].id
                recommendations['recommended_movies'].append(movie_title)
                recommendations['recommended_posters'].append(movie_info.fetch_poster(movie_id))
                recommendations['recommended_overview'].append(overview)
                recommendations['recommended_genre'].append(genre)
                recommendations['recommended_id'].append(int(movie_id))

            self.logger.log("returned recom")
            return recommendations
        
        except Exception as e:
            
            self.logger.log(str(e))
            recommendations = {
                'recommended_movies': [],
                'recommended_posters': [],
                'recommended_overview': [],
                'recommended_genre': [],
                'recommended_id':[]
            }
            return recommendations

