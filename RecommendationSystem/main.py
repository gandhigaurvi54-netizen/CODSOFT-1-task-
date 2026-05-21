from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = [
    "Avengers",
    "IronMan",
    "CaptainAmerica",
    "Batman",
    "Superman"
]

genres = [
    "action marvel hero",
    "action marvel tech",
    "action marvel soldier",
    "action dc dark",
    "action dc flying"
]

cv = CountVectorizer()

matrix = cv.fit_transform(genres)

similarity = cosine_similarity(matrix)

print("Movie Recommendation System")

name = input("Enter movie name: ")

if name in movies:

    index = movies.index(name)

    scores = list(enumerate(similarity[index]))

    scores = sorted(scores, key=lambda x:x[1], reverse=True)

    print("\nRecommended Movies:\n")

    for i in scores[1:4]:
        print(movies[i[0]])

else:
    print("Movie not found")