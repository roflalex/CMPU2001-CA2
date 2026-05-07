# CMPU2001-CA2

A Comparative Study of Hash Map and Trie Data Structures for Efficient Movie Search Using the MovieLens Dataset.

## Overview

This project benchmarks three search strategies — **Trie**, **Hash Table**, and **Linear Search** across scaling subsets of a MovieLens movie dataset (~100k titles). It measures build time, exact-match search time, and prefix search time to empirically demonstrate the performance trade-offs of each data structure.

## Project Structure

```
CMPU2001-Assignment/
├── main.py                    # Benchmark harness
├── data/
│   └── movies.csv             # MovieLens dataset
├── dataloader/
│   └── dataloader.py          # CSV parser and data loader
├── hash/
│   └── hash_table.py          # Hash table with separate chaining
├── trie/
│   ├── trie.py                # Trie implementation
│   └── trie_node.py           # Trie node definition
└── linear/
    └── linear_search.py       # Brute-force baseline
```

## Data Structures

### Trie (Prefix Tree)
- Stores movie titles character-by-character in a tree structure
- Supports **exact search** in O(m) time (m = title length)
- Supports **prefix search** via DFS traversal — returns all matching titles
- Case-insensitive via lowercase normalisation on insert

### Hash Table
- Fixed-size table with **131,071 slots** (a prime number to reduce collisions)
- **Separate chaining** for collision resolution
- Movies are indexed by both **title** and **ID** in the same table
- O(1) average-case exact lookup; no prefix search support

### Linear Search
- Brute-force iteration over the entire movie list
- Supports both **exact** and **prefix** search
- O(n) time complexity — serves as a performance baseline

## Dataset

MovieLens CSV format (`movieId,title,genres`). Year suffixes (e.g. `"Toy Story (1995)"`) are stripped during loading, so titles are stored without the year.

## Running the Benchmark

```bash
python main.py
```

The script loads the full dataset and runs experiments at six dataset sizes:

| Dataset Size |
|-------------|
| 1,000        |
| 5,000        |
| 10,000       |
| 20,000       |
| 40,000       |
| 80,000       |

For each size, three search queries are averaged over three repetitions. The output reports:

- **Build time** — time to populate the Trie and Hash Table
- **Exact search time** — Trie vs Hash Table vs Linear Search
- **Prefix search time** — Trie vs Linear Search

## Algorithm Complexity Summary

| Operation             | Trie         | Hash Table          | Linear Search  |
|-----------------------|--------------|---------------------|----------------|
| Build                 | O(n·m)       | O(n)                | —              |
| Exact search          | O(m)         | O(1) avg / O(n) worst | O(n)         |
| Prefix search         | O(k)         | Not supported       | O(n·m)         |

*m = average title length, n = number of movies, k = number of results in subtree*

## Requirements

- Python 3.x
- No external dependencies (uses only the standard library)
