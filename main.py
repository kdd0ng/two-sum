from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_list = {}
    
    for index, num in enumerate(nums):
        indice = target - num
        if indice in nums_list:
            
            return [nums_list[indice], index]

        nums_list[num] = index
        
    #return
# nums = [2,7,11,15]
# target = 18
# result = twoSum(nums, target)
# print(result)