class LinearSearch:
    def __init__(self, movies):
        self.movies = movies

    def search(self, title):
        for movie in self.movies:
            if movie["title"] == title:
                return movie
        return None

    def prefix_search(self, prefix):
        results = []
        for movie in self.movies:
            if movie["title"].lower().startswith(prefix.lower()):
                results.append(movie)
        return results