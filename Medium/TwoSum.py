class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}                               #Create a map of value to its position
        
        for i,n in enumerate(nums):
            second_val = target - n                 #Second possible member of pair
            if second_val in nums_map:              #If second value is already found
                return (i, nums_map[second_val])    #Return the current pair
            else:
                nums_map[n] = i                     #Append current value and position to map
            
            