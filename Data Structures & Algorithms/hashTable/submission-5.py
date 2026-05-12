class HashNode:
    
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.hashmap = [None] * capacity

    def hash(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        idx = self.hash(key)
        node = self.hashmap[idx]

        if not node:
            newNode = HashNode(key, value)
            self.hashmap[idx] = newNode
            self.size += 1
            if self.size >= self.capacity * 0.5:
                self.resize()
            return

        while node.key != key and node.next:
            node = node.next

        if node.key == key:
            node.value = value
            return

        newNode = HashNode(key, value)
        node.next= newNode
        return

    def get(self, key: int) -> int:
        idx = self.hash(key)
        node = self.hashmap[idx]

        if not node:
            return -1

        while node and node.key != key:
            node = node.next

        if not node:
            return -1
        return node.value

    def remove(self, key: int) -> bool:
        idx = self.hash(key)
        node = self.hashmap[idx]

        if not node:
            return False
         
        if node.key == key:
            self.hashmap[idx] = node.next
            self.size -= 1
            return True

        while node.next and node.next.key != key:
            node = node.next

        if not node.next:
            return False

        node.next = node.next.next
        return True

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        self.size = 0
        copiedHashmap = self.hashmap.copy()
        self.hashmap = [None] * self.capacity

        for node in copiedHashmap:
            if not node:
                continue
            curr = node
            while curr:
                self.insert(curr.key, curr.value)
                curr = curr.next
        return
            

