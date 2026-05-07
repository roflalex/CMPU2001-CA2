from dataloader.dataloader import MovieDataLoader
from hash.hash_table import HashTable
from trie.trie import Trie
from linear.linear_search import LinearSearch
import time

def time_search(fn):
    start = time.perf_counter()
    result = fn()
    end = time.perf_counter()
    return result,end - start

def average(times):
    return sum(times) / len(times)

def experiment(movies, repeats=3):
    #setup searches
    search_titles = ["Toy Story", "Jumanji", "Telly Tubbies"]
    prefix = "Xyz"

    trie_exact_times = []
    hash_exact_times = []
    linear_exact_times = []

    trie_prefix_times = []
    linear_prefix_times = []

    trie_build_times = []
    hash_build_times = []

    #perform searches and get average runtime per search.
    for _ in range(repeats):
        #build structures
        trie = Trie()
        ht = HashTable(size=131071)
        linear = LinearSearch(movies)

        # time trie insertion
        start = time.perf_counter()
        for movie in movies:
            trie.insert(movie["title"], movie)
        trie_build_times.append(time.perf_counter() - start)

        # time Hash insertion
        start = time.perf_counter()
        for movie in movies:
            ht.insert(movie)
        hash_build_times.append(time.perf_counter() - start)

        # exact search for each data structure 
        for title in search_titles:
            _, t = time_search(lambda: trie.search(title))
            trie_exact_times.append(t)

            _, t = time_search(lambda: ht.search(title))
            hash_exact_times.append(t)

            _, t = time_search(lambda: linear.search(title))
            linear_exact_times.append(t)
        # prefix search for tries and linear 
        _, t = time_search(lambda: trie.prefix_search(prefix))
        trie_prefix_times.append(t)

        _, t = time_search(lambda: linear.prefix_search(prefix))
        linear_prefix_times.append(t)
    return {
        "trie_build": average(trie_build_times),
        "hash_build": average(hash_build_times),
        "trie_exact": average(trie_exact_times),
        "hash_exact": average(hash_exact_times),
        "linear_exact": average(linear_exact_times),
        "trie_prefix": average(trie_prefix_times),
        "linear_prefix": average(linear_prefix_times)
    }
def main():
    print("Loading movies...\n")

    loader = MovieDataLoader("data/movies.csv")
    all_movies = loader.load_movies()

    dataset_sizes = [1000, 5000, 10000, 20000, 40000, 80000]

    print("-"*60,"\nScaling Experiment Results\n","-"*60)

    for size in dataset_sizes:
        movies = all_movies[:size]

        start = time.perf_counter()
        results = experiment(movies)
        total_time = time.perf_counter() - start

        print(f"\nDataset Size: {size}")
        print(f"Trie Build Avg: {results['trie_build']:.6f}")
        print(f"Hash Build Avg: {results['hash_build']:.6f}")

        print(f"Trie Exact Avg:   {results['trie_exact']:.8f}")
        print(f"Hash Exact Avg:   {results['hash_exact']:.8f}")
        print(f"Linear Exact Avg: {results['linear_exact']:.8f}")

        print(f"Trie Prefix Avg:   {results['trie_prefix']:.8f}")
        print(f"Linear Prefix Avg: {results['linear_prefix']:.8f}")

if __name__ == "__main__":
    main()