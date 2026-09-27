class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            minheap.append((dist, x, y))

        heapq.heapify(minheap)

        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(minheap)
            result.append([x, y])

        return result