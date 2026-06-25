class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)

        ans = -1
        for i, j in counter.items():
            if i == j:
                ans = max(ans, i)
        return ans