class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        arr = list()
        for i, j in count.items():
            if j > (len(nums)/3):
                arr.append(i)
        
        return arr