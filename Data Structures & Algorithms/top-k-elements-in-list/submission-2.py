class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        # arr = list()
        # for i, j in counter.items():
        #     if j >= k:
        #         arr.append(i)
        
        # return arr

        return [num for num, freq in counter.most_common(k)]