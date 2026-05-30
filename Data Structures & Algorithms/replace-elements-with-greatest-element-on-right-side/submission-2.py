class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(0, len(arr)):
            remain_nums = arr[i+1:]
            
            if remain_nums:
                max_num = max(remain_nums)
            
                arr[i] = max_num
        
        arr[-1] = -1
        return arr