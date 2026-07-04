import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Hello, Welcome to the recommenation System.\n")
print("What Can I recommend you?")
print("Books")
print("Movies")
ch = input("Enter your choice: ")
if ch.lower() == "movies":
    movies = pd.read_csv("movies.csv")
    movies["Description"] = movies["Description"].fillna("")

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(movies["Description"])

    similarity = cosine_similarity(tfidf_matrix)

    def recommend(movie_name):

        if movie_name not in movies["title"].values:
            print("Sorry there aren't any movies as per your taste :(")
            return

        movie_index = movies[movies["title"] == movie_name].index[0]

        scores = list(enumerate(similarity[movie_index]))

        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        for movie in scores[1:6]:
            print(movies.iloc[movie[0]]["title"])

    movie_name = input("Enter a movie Name: ")
    print("Top movies which you should watch if you liked", movie_name)
    recommend(movie_name)

    while True:

        print("Want more recommendation?")
        print("1 for yes and 0 to end")
        choice = int(input("Enter your choice: "))

        if choice == 1:

            movie_name = input("Enter a movie Name: ")
            print("Top 5 movies which you should watch if you liked", movie_name)
            recommend(movie_name)

        elif choice == 0:

            print("Thanks for using, I hope you liked these recommendations.")
            break

        else:
            print("Plese enter valid choice!")
elif ch.lower() == "books":
    books = pd.read_csv("books.csv")
    books["Genre"] = books["Genre"].fillna("")

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(books["Genre"])

    similarity = cosine_similarity(tfidf_matrix)

    def recommend(book_name):

        if book_name not in books["Name"].values:
            print("Sorry there aren't any Books as per your taste :(")
            return

        book_index = books[books["Name"] == book_name].index[0]

        scores = list(enumerate(similarity[book_index]))

        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        for book in scores[1:6]:
            print(books.iloc[book[0]]["Name"])

    book_name = input("Enter a Book Name: ")
    print("Top Books which you should read if you liked", book_name)
    recommend(book_name)

    while True:

        print("Want more recommendation?")
        print("1 for yes and 0 to end")
        choice = int(input("Enter your choice: "))

        if choice == 1:

            book_name = input("Enter a Book Name: ")
            print("Top Books which you should read if you liked", book_name)
            recommend(book_name)

        elif choice == 0:

            print("Thanks for using, I hope you liked these recommendations.")
            break

        else:
            print("Plese enter valid choice!")







