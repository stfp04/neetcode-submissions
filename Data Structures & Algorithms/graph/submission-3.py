class Graph:
    
    def __init__(self):
        self.vertex = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.vertex:
            self.vertex[src] = set()
        if dst not in self.vertex:
            self.vertex[dst] = set()
        self.vertex[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.vertex:
            return False
        if dst not in self.vertex:
            return False
        self.vertex[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        queue = deque()
        queue.append(src)
        while queue:
            for _ in range(len(queue)):
                vertex = queue.popleft()
                for v in self.vertex[vertex]:
                    if v == dst:
                        return True
                    if v in visit:
                        continue

                    queue.append(v)
                    visit.add(v)
        return False

