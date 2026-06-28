class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        r = []
        for i in range(n):
            for j in range(i+1, n):
                diff = abs(i - j)
                ans = min(heights[i], heights[j]) * diff
                r.append(ans)

        return max(r)
