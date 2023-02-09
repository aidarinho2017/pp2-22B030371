movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def above_5_5(movie):
    if movie["imdb"] > 5.5:
        return True
    else:
        return False

def sublist_movies(movies):
    sublist = []
    for movie in movies:
        if above_5_5(movie):
            sublist.append(movie)
    return sublist

def category_movies(category, movies):
    sublist = []
    for movie in movies:
        if movie["category"] == category:
            sublist.append(movie)
    return sublist

def average_imdb(movies):
    total_score = 0
    for movie in movies:
        total_score += movie["imdb"]
    return total_score / len(movies)

def average_category_imdb(category, movies):
    category_movies = category_movies(category, movies)
    return average_imdb(category_movies)
