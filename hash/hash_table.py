class HashTable:
    def __init__(self,size=131071):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0

    def hash(self,key):
        return hash(key) % self.size
    
    def insert(self,movie):
        key = movie["title"]
        index = self.hash(key)

        if len(self.table[index]) > 0:
            self.collisions +=1

        self.table[index].append(movie)
    def search(self,title):
        index = self.hash(title)
        
        for movie in self.table[index]:
            if movie["title"] == title:
                return movie
        return None