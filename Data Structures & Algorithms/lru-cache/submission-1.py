class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.LRU = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.LRU.remove(key)
            self.LRU.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.LRU.remove(key)
            self.LRU.append(key)
        else:
            if len(self.cache) >= self.capacity:
                keyToRemove = self.LRU.pop(0)
                self.cache.pop(keyToRemove)

            self.LRU.append(key)
            self.cache[key] = value
        print(self.LRU)
