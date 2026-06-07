class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_nums = Counter(nums)

        for v, x in counter_nums.items():
            if x > (len(nums)/2):
                return v 