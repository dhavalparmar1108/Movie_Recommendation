from flask import Flask, request, jsonify
from utils.utility import Utility
import logging

app = Flask(__name__)
  
@app.route('/fetch-movies', methods=["GET"])
def fetch_movies():
    try:
        name = request.args.get('name')
    
        if not name:
            return jsonify({"error": "No movie name provided", "status": 400}), 400

        movie_utility = Utility()
        recommendedations = movie_utility.recommend(name)
        
        print(recommendedations)
        
        if not recommendedations['recommended_id']:
            return jsonify({"error": "Movie not found" , "status":404}), 404

        return jsonify({
            "status" : 200,
            "recommendations": recommendedations,
        })
    except Exception as e:
        logging.info("Error " + str(e))
        return jsonify({"error": str(e), "status": 400}), 400
    

@app.route('/fetch-suggestions', methods=["GET"])
def fetch_suggestions():
    name = request.args.get('name')
    movie_utility = Utility()
    suggestions = movie_utility.getSuggestion(name)
    return jsonify({
        "status" : 200,
        "recommended_movies": suggestions,
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

   
