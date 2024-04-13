# There is an undirected graph of n nodes. You are given a 2D array edges, where edges[i] = [ui, vi, lengthi] describes an edge between node ui and node vi with a traversal time of lengthi units.

# Additionally, you are given an array disappear, where disappear[i] denotes the time when the node i disappears from the graph and you won't be able to visit it.

# Notice that the graph might be disconnected and might contain multiple edges.

# Return the array answer, with answer[i] denoting the minimum units of time required to reach node i from node 0. If node i is unreachable from node 0 then answer[i] is -1.

from collections import defaultdict, deque
from typing import List

# class Solution:
#     def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
#         graph = defaultdict(list)
#         for u, v, l in edges:
#             graph[u].append((v, l))
#             graph[v].append((u, l))
#         answer = [-1] * n
#         answer[0] = 0
#         q = deque([0])
#         while q:
#             u = q.popleft()
#             for v, l in graph[u]:
#                 print("u:", u)
#                 print("VL:", v, l)
#                 if answer[u] + l >= disappear[v]:
#                     continue
#                 if answer[v] == -1 or answer[v] > answer[u] + l:
#                     answer[v] = answer[u] + l
#                     q.append(v)
#         return answer
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))

        dist = [-1] * n
        pq = [(0, 0)]  # (distance, node)
        dist[0] = 0

        while pq:
            d, u = heapq.heappop(pq)
            if d > disappear[u]:
                continue
            for v, length in graph[u]:
                if disappear[v] <= d:
                    continue
                if dist[v] == -1 or d + length < dist[v]:
                    dist[v] = d + length
                    heapq.heappush(pq, (dist[v], v))

        return dist
        # graph = defaultdict(list)
        # for u, v, l in edges:
        #     graph[u].append((v, l))
        #     graph[v].append((u, l))
        
        # answer = [-1] * n
        # answer[0] = 0
        
        # disappear_order = sorted(range(n), key=lambda x: disappear[x])
        
        # q = deque([0])
        # while q:
        #     u = q.popleft()
        #     for v, l in graph[u]:
        #         if answer[u] + l >= disappear[v]: 
        #             continue
        #         if answer[v] == -1 or answer[v] > answer[u] + l:
        #             answer[v] = answer[u] + l
        #             q.append(v)
        #     q = deque(sorted(q, key=lambda x: disappear_order[x]))

        # return answer
    
# n = 3
# edges = [[0,1,2],[1,2,1],[0,2,4]]
# disappear = [1000000,100000000,5]

# test case failed
n = 2
edges = [[0, 1, 1]]
disappear = [1, 1]
x = Solution()
print(x.minimumTime(n, edges, disappear)) # [0, -1]