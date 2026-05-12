class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()

        def hasCycle(node, adjList, path) -> bool:
            nonlocal visit
            for neighbour in adjList[node]:
                if neighbour in path:
                    return True
                visit.add(neighbour)
                path.add(neighbour)
                cycle = hasCycle(neighbour,adjList,path)
                if cycle:
                    return True
                path.remove(neighbour)
            return False
                

        if not prerequisites:
            return True
        adjList = {i: set() for i in range(numCourses)}
        
        for a,b in prerequisites:
            adjList[a].add(b)

        for course in adjList:
            if course in visit:
                continue
            path = {course}
            cycle = hasCycle(course, adjList, path)
            if cycle:
                return False
        return True
        