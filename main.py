from dataloader.dataloader import MovieDataLoader
from hash.hash_table import HashTable
from trie.trie import Trie
import time


'''
TODO:
Implement Hashmap for exact movie lookup
Implement Prefix trie for prefix based search and autocomplete functionality

Evaluate their performance on searching for movies by exact title or ID
Evaluate their performance on searching for prefix-based searches on movie titles
Evaluate the performance of inserting movie records into each data structure
Evaluate the performance of retrieving matching multiple results for patrial queries

Analyse and compare performance of each data strucutre against their theoretical time complexities

Design and conduct controlled experiments to measure and compare runtime performance across different query types and dataset operations



'''
def time_search(fn):
    start = time.perf_counter()
    result = fn()
    end = time.perf_counter()
    return result,end - start

def main():
    print("Loading movies...\n")

    loader = MovieDataLoader("data/movies.csv")
    movies = loader.load_movies()

    
    #Build Trie
    trie = Trie()
    for movie in movies:
        trie.insert(movie["title"],movie)

    print(f"Inserted into Trie: {len(movies)} movies\n")
    search_titles = [
        "Toy Story",
        "Jumanji",
        "Telly Tubbies vs Power Rangers"
    ]

    print("-"*50,"\nTrie search\n"+"-"*50)
    
    for title in search_titles:
        movie, duration = time_search(lambda: trie.search(title))
        if movie:
            print(f"{title}: Found ({duration:.6f} sec) → Genres: {movie['genres']}")
        else:
            print(f"{title}: Not Found ({duration:.6f} sec)")

    # Prefix search demo
    print("\nPrefix search: 'Toy'\n")
    results = trie.prefix_search("Toy")

    for movie in results[:5]:
        print(f"{movie['title']} → {movie['genres']}")
        
    print("-"*50,"\nTrie Autocomplete\n"+"-"*50)

    prefixes = ["Toy", "Ju", "Star"]

    for prefix in prefixes:
        results, duration = time_search(lambda: trie.autocomplete(prefix))

        print(f"\nPrefix '{prefix}' ({duration:.6f} sec):")

        if results:
            for movie in results[:5]:  # limit output
                print(f"  {movie['title']} → {movie['genres']}")
        else:
            print("  No matches found")
    #Build hash table
    ht = HashTable(size=131071)

    for movie in movies:
        ht.insert(movie)
    print(f"\nInserted: {len(movies)} movies")
    print(f"Collisions:{ht.collisions}\n")

    # Hash table search timing 
    print(f"-"*50,"\nHash table search\n"+"-"*50)
    for title in search_titles:
        movie,duration = time_search(lambda:ht.search(title))
        if movie:
            print(f"{title}: Found ({duration:.6f} sec) →Genres: {movie['genres']}")
        else:
            print(f"{title}: Not Found ({duration:.6f} sec)")    
if __name__ == "__main__": 
    main()