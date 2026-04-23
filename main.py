from dataloader.dataloader import MovieDataLoader

def main():
    print("Loading movies...\n")

    loader = MovieDataLoader("data/movies.csv")
    movies = loader.load_movies()

    for movie in movies[:5]:
        print(movie)

    print(f"\nTotal movies loaded: {len(movies)}")
    
if __name__ == "__main__": 
    main()