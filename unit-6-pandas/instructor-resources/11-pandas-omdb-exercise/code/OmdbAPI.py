import requests
import pandas as pd

class Omdb:
    '''
    Python API for OMBD API. Please obtain an API key here: http://www.omdbapi.com/apikey.aspx
    To use, instantiate a class like so:
    my_call = Omdb(movies, 'e55xe9e9')
    
    -- Instantiating a class
    movies<dataframe>: a dataframe. Must have the columns 'year' and 'title'. 
    If your df differs, set the private class properties self.yearcol
    and self.titlecol appropriately.
    'e55xe9e9'<string>: this is an example api key
    class properties: these have been set as properties as convenience to
    allow the user to avoid refactoring the class as the API evolves.
    
    -- Calling the API
    Use the .get_ratings() class method. It will look up the movie by year
    and title and return the IMDB ID. It will then make another call to the API,
    by IMDB ID, which is needed to retrieve the ratings details. There is no
    way at the time of writing to call the API with more than one movie. Also,
    note that each movie rating requires 2 calls to the API. A free token at 
    the time of writing allows 1,000 calls per day. Therefore, you may retrieve
    a maximum of 500 movie ratings per day with this script and a free API token.
    '''
    
    def __init__(self, df, apikey):

        # public user variables
        self.df = df.copy()
        self.apikey = apikey
        
        # private user varibles
        self.yearcol = 'year'
        self.titlecol = 'title'
        
        # private api variables
        self.endpoint = 'http://www.omdbapi.com/'
        self.apikey_param = 'apikey'
        self.search_param = 's'
        self.year_param = 'y'
        self.id_param = 'i'
        # RATINGS: used for parsing json query response when using imdbRating, get_ratings()
        self.imdbRating = 'imdbRating'
        self.Ratings = 'Ratings'
        self.Source = 'Source'
        self.Value = 'Value'
        # ID: used for parsing json query response when using imdbID, __get_imdb_id
        self.Search = 'Search'
        self.imdb_id_idx = 0 # take the first result, this is a hack since we are not checking for multiple results
        self.imdbID = 'imdbID'

    def __get_imdb_id(self, year, title):
        '''
        Private method. Retrieves the IMDB ID for the movie
        which is needed to retrieve the detailed rating review numbers.
        '''
        return requests.get(
                self.endpoint, 
                params={
                    self.apikey_param : self.apikey, 
                    self.search_param : title, 
                    self.year_param : year}
                ).json()[self.Search][self.imdb_id_idx][self.imdbID]
        
    def get_ratings(self):
        '''
        Returns: dataframe with all ratings from every source for each movie.
        Result is joined with the original dataframe from which the class 
        was instantiated, with the ratings columns added to the end.
        Datatype and source may vary as the API evolves.
        '''
        buf = {}
        for idx, year, title in zip(self.df.index, 
                                    self.df[self.yearcol], 
                                    self.df[self.titlecol]):
            # catch for the two API calls
            try:
                # call the api by ID for verbose rating information
                # which calls __get_imdb_id api by search for the ID info
                res = (requests.get(
                    self.endpoint, 
                    params={self.apikey_param: self.apikey, 
                            self.id_param: self.__get_imdb_id(year, title)
                           }).json()
                )
                # iterate through each of the rating authorities for a given ID
                buf[idx] = {}
                # catch for parsing the ratings for the results from the api calls
                try:
                    for source in res[self.Ratings]:
                        buf[idx].update({source[self.Source]: source[self.Value]})
                except:
                    continue
            except:
                continue
               
#        return buf
        return pd.merge(self.df, 
                        pd.DataFrame.from_dict(buf, orient='index'),
                        how='left', 
                        left_index=True, 
                        right_index=True) 


def main():

    '''
    Not implemented
    '''
    print('Not intended to be run as a script, exiting...')

if __name__ == "__main__":
    main()
