import re

class MovieDataLoader:
    def __init__(self,filepath,delimiter = ','):
        self.filepath = filepath
        self.delimiter = delimiter
        self.movies = []
        
    def load_movies(self):
        with open(self.filepath,'r',encoding='utf-8') as file:
            next(file)

            for line in file:
                parts=line.strip().split(',')

                if len(parts)<3:
                    continue
                movie_id = int(parts[0])
                title = self._clean_title(parts[1])
                genres = parts[2].split('|')

                self.movies.append({
                    "id":movie_id,
                    "title":title,
                    "genres":genres
                })

            return self.movies
    def _clean_title(self,title):
        """Remove year from movie title"""
        data = re.sub(r'\s*\(\d{4}\)\s*$', '', title).strip()
        return data