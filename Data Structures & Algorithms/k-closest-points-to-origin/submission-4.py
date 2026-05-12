class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        distances = []

        for point in points:
            x, y = point
            distance = math.sqrt( (x - 0) ** 2 + (y - 0)**2 )
            if len(distances) < k:
                distances.append(distance)
                heap.append(point)

                idx = len(distances) - 1
                while (idx-1) // 2 >= 0:
                    if distances[idx] <= distances[(idx-1)//2]:
                        break

                    tmp = distances[idx]
                    distances[idx] = distances[(idx-1)//2]
                    distances[(idx-1)//2] = tmp

                    tmp = heap[idx]
                    heap[idx] = heap[(idx-1)//2]
                    heap[(idx-1)//2] = tmp

                    idx = (idx-1)//2
            else:
                if distance >= distances[0]:
                    continue

                distances[0] = distance
                heap[0] = point

                idx = 0
                while idx * 2 + 1 < len(distances):
                    if idx*2 + 2 < len(distances) and \
                    distances[idx*2+2] > distances[idx*2+1] and \
                    distances[idx*2+2] > distances[idx]:
                        tmp = distances[idx*2+2]
                        distances[idx*2+2] = distances[idx]
                        distances[idx] = tmp

                        tmp = heap[idx*2+2]
                        heap[idx*2+2] = heap[idx]
                        heap[idx] = tmp

                        idx = idx*2+2
                    elif distances[idx*2+1] > distances[idx]:
                        tmp = distances[idx*2+1]
                        distances[idx*2+1] = distances[idx]
                        distances[idx] = tmp

                        tmp = heap[idx*2+1]
                        heap[idx*2+1] = heap[idx]
                        heap[idx] = tmp

                        idx = idx*2+1
                    else:
                        break
        return heap


























