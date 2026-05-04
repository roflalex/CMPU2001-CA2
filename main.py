from dataloader.dataloader import MovieDataLoader
from hash.hash_table import HashTable
from trie.trie import Trie
import time

def time_search(fn):
    start = time.perf_counter()
    result = fn()
    end = time.perf_counter()
    return result,end - start

def main():
    print("Loading movies...\n")

    loader = MovieDataLoader("data/movies.csv")
    movies = loader.load_movies()

    '''
    Build Trie
    '''
    
    trie = Trie()
    start = time.perf_counter()
    for movie in movies:
        trie.insert(movie["title"],movie)
    trie_build_time = time.perf_counter() - start

    print(f"Trie insert time: {trie_build_time:.6f} sec")

    ''' 
    Build hash
    '''

    ht = HashTable(size=131071)
    start = time.perf_counter()
    for movie in movies:
        ht.insert(movie)
    hash_build_time = time.perf_counter() - start

    print(f"Hash insert time: {hash_build_time:.6f} sec")
    print(f"Collisions: {ht.collisions}\n")

    '''
    Exact Search
    '''

    search_titles = [
        "Toy Story",
        "Jumanji",
        "Telly Tubbies vs Power Rangers"
    ]

    print("-"*50,"\nExact Search Comparison\n"+"-"*50)

    for title in search_titles:
        t_movie, t_time = time_search(lambda: trie.search(title))
        h_movie, h_time = time_search(lambda: ht.search(title))

        print(f"\n{title}")
        print(f"Trie: {'Found' if t_movie else 'Not Found'} ({t_time:.6f})")
        print(f"Hash: {'Found' if h_movie else 'Not Found'} ({h_time:.6f})")

    '''
    ID Search
    '''
    print("\n"+"-"*50,"\nID Search\n"+"-"*50)

    test_ids = [1, 50, 999999]

    for movie_id in test_ids:
        movie, duration = time_search(lambda: ht.search(movie_id))

        if movie:
            print(f"{movie_id}: Found ({duration:.6f}) → {movie['title']}")
        else:
            print(f"{movie_id}: Not Found ({duration:.6f})")

    '''
    Prefix Search
    '''
    print("\n"+"-"*50,"\nPrefix Search\n"+"-"*50)

    prefixes = ["Toy", "Ju", "Star"]

    for prefix in prefixes:
        results, duration = time_search(lambda: trie.prefix_search(prefix))

        print(f"\nPrefix '{prefix}' ({duration:.6f})")

        if results:
            print(f"Matches: {len(results)}")
            for movie in results[:5]:
                print(f"  {movie['title']}")
        else:
            print("No matches")
    
'''
Conclusion:
    Hash Table:
    Avg O(1) search, collisions affect performance

    Trie:
    O(k) search where k = length of title/prefix
    Better for prefix queries
'''
if __name__ == "__main__": 
    main()