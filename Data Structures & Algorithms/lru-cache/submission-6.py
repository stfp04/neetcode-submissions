class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.t = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.t += 1
            self.cache[key][1] = self.t
            print(self.cache)
            return self.cache[key][0]
        print("Not in cache")
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            lru, t = None, float('inf')
            for k, (v, ti) in self.cache.items():
                if ti >= t:
                    continue
                lru = k
                t = ti
            self.cache.pop(lru)

        self.t += 1
        self.cache[key] = [value, self.t]
        print(self.cache)
        return
