from flask import Flask, render_template, request
import requests
import sys

app = Flask(__name__)


class OMDBError(Exception):
    """
    OMDBError represents an error returned by the OMDb API.
    """
    pass


class Movie(object):
    """
    `Movie` objects contain all information about a particular movie,
    including the title and rating.
    """

    def __init__(self, movie_data):

        # Store the raw data from OMDb in this object so that we can use the
        # data in the getter functions.
        self.omdb_data = movie_data

    def get_movie_title(self):
        """
        `get_movie_title` is a getter function that returns the movie title.
        """

        # Return the title from the movie data.
        return self.omdb_data["Title"]

    def get_movie_rating(self, source="Rotten Tomatoes"):
        """
        get_movie_rating is a getter function that returns the rating.
        """

        # There can be multiple ratings for each movie, so they are stored as a
        # list of ratings, each with a source and a rating. By default, we are
        # only interested in Rotten Tomatoes ratings, so we loop through each
        # rating and return it if the source is Rotten Tomatoes.
        for ratings in self.omdb_data["Ratings"]:
            if ratings["Source"] == source:
                return ratings["Value"]

        # If the code makes it here, it hasn't returned in the `for` loop.
        return f'- Wait - Rating for source {source} was not found!'


class OMDB(object):
    """
    OMDb objects represent clients to the OMDb API. It has helper methods for
    performing functions on the API.
    """
    def __init__(self, apikey):
        # Store the API key so it may be used later to build the authenticated URL.
        self.apikey = apikey
        self.url = "http://www.omdbapi.com/?"

    def call_api(self, **kwargs):
        """
        `call_api` uses the provided parameters to create a URL to the OMDb API,
        call the API, parse the results, and return the parsed JSON data.

        If the API returns an error, the error is raised as an exception.
        """

        # Add the API key to the dictionary of parameters to send to OMDb.
        kwargs["apikey"] = self.apikey

        # Call the API and return the raw result
        response = requests.get(self.url, kwargs)

        # Check for an error and throw an exception if needed
        if response.status_code != requests.codes.ok:
            raise OMDBError(response.json()['Error'])
            sys.exit(1)

        # Use `json()` to decode the raw JSON data.
        response_data = response.json()

        # Return the decoded data.
        return response_data

    def get_movie(self, movie_query):
        """
        Get a `Movie` object containing all the data for a single movie. Returns
        a single `Movie` object.
        """
        # Call the API, passing the movie_query as "t" (by title).
        movie_data = self.call_api(t=movie_query)

        # Create a `Movie` with the raw results from the API call.
        return Movie(movie_data)

    def search(self, movie_query):
        """
        Search for movies based on keywords. Returns list of dictionaries.
        """
        # Call the API, passing the movie_query as "s" (by search).
        movie_dictionaries = self.call_api(s=movie_query)

        # Return the list of movie dictionaries.
        return movie_dictionaries["Search"]

    def get_movie_by_id(self, id):
        """
        Get a `Movie` object containing all the data for a single movie. Returns
        a single `Movie` object.
        """
        # Call the API, passing the query as "i" (by `id`).
        data = self.call_api(i=id)

        # Create a `Movie` with the raw results from the API call.
        return Movie(data)


def get_apikey():
    """
    Read API key from file on disk.
    """

    # Open file in read mode (r).
    with open("omdb-api-key.txt", "r") as file:

        # Read the file into a variable (key).
        key = file.read()

        # Strip any whitespace characters such as a newline that may be present
        # in the file.
        key = key.strip()

        # Return the key.
        return key


def list_search_results(movie_to_look_up):
    """
    Prompt for search term and print list of matching movies.
    """

    # Read the API key from disk.
    apikey = get_apikey()

    # Create OMDb client with the provided API key.
    omdb = OMDB(apikey)

    # Get results from the OMDb API. If OMDb error occurs, print the error message and exit.
    try:
        matching_movie_list = omdb.search(movie_to_look_up)
    except OMDBError as err:
        print(f'OMDB Error: {err}')
        return

    # Extract titles from the search result list with list comprehension (each
    # result is a dictionary).
    movie_titles = [each_movie["Title"] for each_movie in matching_movie_list]

    # Loop through the list of titles and print them (indented with four spaces).
    for title in movie_titles:
        print("    " + title)


def return_single_movie_object(movie_to_look_up):
    """
    Prompt for movie title and return the movie object.
    """

    # Read the API key from disk.
    apikey = get_apikey()

    # Create OMDB client with the provided API key.
    omdb = OMDB(apikey)

    # Get `Movie` object. If OMDb error occurs, print the error message and exit.
    try:
        my_movie_object = omdb.get_movie(movie_to_look_up)
        return my_movie_object
    except OMDBError as err:
        print(f'OMDB Error: {err}')
        return

def print_single_movie_rating(movie_query):
    """
    Create a `Movie` object and print one movie's Rotten Tomatoes rating.
    """

    my_movie = return_single_movie_object(movie_query)

    # Print the rating. Note that we have to escape the quotes around the movie
    # title because those quotes are inside a string that also uses quotes.
    print(f'The rating for {my_movie.get_movie_title()} is {my_movie.get_movie_rating()}.')

def print_all_ratings(movie_list):
    """
    Take in a list of movies, create a `Movie` object for each, and print the rating.
    """
    for movie in movie_list:
        movie_object = return_single_movie_object(movie)
        print("The movie", movie_object.get_movie_title(), "has a rating of", movie_object.get_movie_rating())















# Create one main function that will call everything else.
def main():
    app.run(debug=True)

@app.route("/", methods=["GET"])
def home():
    # whatever = input("put something here")
    # Read the API key from disk.
    apikey = get_apikey()

    # Create OMDb client with provided API key.
    omdb = OMDB(apikey)

    # Get the search query from the form.
    movie_query = request.args.get("query", "")

    print("Query is:", movie_query)

    # If a query is present, get search results from OMDb and render template.
    if movie_query:
        matching_movie_list = omdb.search(movie_query)
        movie_titles = [each_movie["Title"] for each_movie in matching_movie_list]
        return render_template("home.html", query=movie_query, results=matching_movie_list)
        # return render_template("home.html", query=movie_query, results=matching_movie_list)

    # # Render page without query/results.
    return render_template("home.html")
    # return "hello"

@app.route("/movies/<id>", methods=["GET"])
def movie(id):
    # Read the API key from disk.
    apikey = get_apikey()

    # Create OMDb client with provided API key.
    omdb = OMDB(apikey)

    # Get the movie from OMDb and gather needed data for template.
    # Ideally we would catch any exceptions in the following and return an
    # appropriate error page. For now it will just throw a regular HTTP 500 if
    # any errors occur.
    movie = omdb.get_movie_by_id(id)
    title = movie.omdb_data["Title"]
    year = movie.omdb_data["Year"]
    poster = movie.omdb_data["Poster"]
    plot = movie.omdb_data["Plot"]

    # `movie.get_rating()` often errors due to no rating present, so we will
    # catch this error specifically.
    try:
        rating = movie.get_movie_rating()
    except OMDBError:
        rating = "(unavailable)"

    # Render template with all needed variables.
    return render_template("movie.html", title=title, year=year, poster=poster, plot=plot, rating=rating)

if __name__ == "__main__":
    main()
