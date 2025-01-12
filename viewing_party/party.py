#from Collections import Counter

# WAVE 1 FUNCTIONS:

# function to create new movie dictionary object
def create_movie(movie_title, genre, rating):
    if (movie_title and genre and rating):
        return { "title":movie_title, "genre":genre, "rating":rating}
    return None

# function to add movie to 'watched' movie list
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    
# function to add movie to 'watchlist'
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# function moves movies from 'watchlist' to 'watched'
def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            # add movie to watched
            user_data["watched"].append(movie)
            #remove movie from watchlist
            user_data["watchlist"].remove(movie)
    return user_data



# WAVE 2 FUNCTIONS:

# function that returns average of 'watched' movie ratings
def get_watched_avg_rating(user_data):
    if user_data["watched"]:
        my_ratings = [movie["rating"] for movie in user_data["watched"]]
        avg_rating = sum(my_ratings) / len(my_ratings)
        return avg_rating
    return 0.0

# QUESTION: AM I ALLOWED TO IMPORT COUNTER FROM COLLECTIONS?
# def get_most_watched_genre(user_data):
#     genre_frequency = []
#     for movie in user_data["watched"]:
#         genre_frequency.append(movie["genre"])
#     genre_counter = Counter(genre_frequency)
#     most_frequent_genre = max(genre_counter, key=genre_counter.get)
#     return most_frequent_genre

# function that returns the most-watched genre
def get_most_watched_genre(user_data):
    if user_data["watched"]:
        # create dictionary with genre and count values
        genre_frequency = {}
        for movie in user_data["watched"]:
            if movie["genre"] in genre_frequency:
                genre_frequency[movie["genre"]] += 1
            else:
                genre_frequency[movie["genre"]] = 1
        most_frequent_genre = max(genre_frequency, key=genre_frequency.get)
        return most_frequent_genre
    return None



# WAVE 3 FUNCTIONS

# get a list of watched movies unique to user (and not friend)
def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched= [movie for friend in user_data["friends"] for movie in friend["watched"]]
    # add movie to new list if friends have not watched it
    unique_user_movies = [movie for movie in user_watched if movie not in friends_watched]
    return unique_user_movies

# get a list of unique movies watched by friends
def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = [movie for friend in user_data["friends"] for movie in friend["watched"]]
    unique_friend_movies = []
    for movie in friends_watched:
        # add movie if user has not watched it and it is not already in list
        if (movie not in user_watched and movie not in unique_friend_movies):
            unique_friend_movies.append(movie)
    return unique_friend_movies



# WAVE 4 FUNCTIONS

# function that returns recommendations from friends based on available subs
def get_available_recs(user_data):
    subscriptions = user_data["subscriptions"]
    watched_titles = [movie["title"] for movie in user_data["watched"]]
    recommendations = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (movie["host"] in subscriptions and 
                movie not in recommendations and 
                movie["title"] not in watched_titles):
                    recommendations.append(movie)
    return recommendations



# WAVE 5 FUNCTIONS

# function that returns recommendations based on fave genre and friends' viewing
def get_new_rec_by_genre(user_data):
    genre = get_most_watched_genre(user_data)
    user_watched = user_data["watched"] 
    friends_watched = [movie for friend in user_data["friends"] for movie in friend["watched"]] 
    recommendations = []
    for movie in friends_watched:
        if (movie not in user_watched and 
            movie not in recommendations and
            movie["genre"] == genre):
                recommendations.append(movie)
    return recommendations

# function that gives a recommendation from user's favorites that friends \
#       haven't already seen
def get_rec_from_favorites(user_data):
    user_favorites = user_data["favorites"]
    friends_watched = [movie for friend in user_data["friends"] for movie in friend["watched"]]
    recommendations = []
    for movie in user_favorites:
        if (movie not in recommendations and movie not in friends_watched):
            recommendations.append(movie)
    return recommendations
