# You are given a 2D integer array points, where points[i] = [xi, yi]. You are also given an integer w. Your task is to cover all the given points with rectangles.

# Each rectangle has its lower end at some point (x1, 0) and its upper end at some point (x2, y2), where x1 <= x2, y2 >= 0, and the condition x2 - x1 <= w must be satisfied for each rectangle.

# A point is considered covered by a rectangle if it lies within or on the boundary of the rectangle.

# Return an integer denoting the minimum number of rectangles needed so that each point is covered by at least one rectangle.

# Note: A point may be covered by more than one rectangle.

class Solution:
    def minRectanglesToCoverPoints(self, points: list[list[int]], w: int) -> int:
        sortedPoints = sorted(points, key=lambda x: (x[0], x[1]))
        count = 1
        prev = sortedPoints[0]
        for i in range(1, len(sortedPoints)):
            if sortedPoints[i][0] - prev[0] > w:
                count += 1
                prev = sortedPoints[i]
        return count
# x = Solution()
# points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
# w = 2
# print(x.minRectanglesToCoverPoints(points, w)) # 2