class HashTable:
    def __init__(self,size=131071):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0