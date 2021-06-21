class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(arr, low, high, x):
 
            # Check base case
            if high >= low:

                mid = (high + low) // 2

                # If element is present at the middle itself
                if arr[mid] == x:
                    return mid

                # If element is smaller than mid, then it can only
                # be present in left subarray
                elif arr[mid] > x:
                    return binary_search(arr, low, mid - 1, x)

                # Else the element can only be present in right subarray
                else:
                    return binary_search(arr, mid + 1, high, x)

            else:
                # Element is not present in the array
                return -1
 
        if not nums or len(nums)==0:
            return None
        elif len(nums)==1:
            return 0 if nums[0]==target else -1
        
        end = 0
        while end < len(nums) - 1 and nums[end]<nums[end+1]:
            end += 1
        start = (end + 1)%len(nums)
        
        if target >= nums[start] and target <= nums[-1]:
            return binary_search(nums, start, len(nums)-1, target)
        else:
            return binary_search(nums, 0, end, target)
        