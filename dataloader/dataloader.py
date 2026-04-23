import re

class MovieDataLoader:
    def __init__(self,filepath,delimiter = ','):
        self.filepath = filepath
        self.delimiter = delimiter
        self.movies = []