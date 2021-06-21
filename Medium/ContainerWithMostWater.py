class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #Brute-force - Try all combinations. Simple? 
        # max_area = 0
        # i = 0
        # while i<len(height)-1:
        #     j = i + 1
        #     while j<len(height):
        #         h = min(height[i], height[j])
        #         area = h * (j - i)
        #         max_area = max(max_area, area)
        #         j += 1
        #     i += 1
        # return max_area
    
    #Its O(n^2) .. Let's look for a linear approach? O(n) 
    #Lets consider the 2 pointer approach!! 
    #Where should we start the pointers?
    #Maximizing area is basically maximizing the combination of heights of borders and the width i.e the height     #between two borders
    #So if we should start l and r at max width
    
        l, r = 0, len(height) - 1  # Start pointers at extreme positions
        max_area = 0
        
        while l<r:
            area = min(height[l], height[r]) * (r - l)          #Get the area by multiplying minimum of borders' height with width
            max_area = max(area, max_area)                      #Update the max_area
            if height[l]<height[r]:                             #Update the pointer which has less length so that we can go for a potentially larger height border in next iteration
                l += 1
            else:
                r -= 1                                          #Remember this is valid when height of right side is small but also valid when both heights are equal(It does not really matter which side you increment when both are equal.)
        return max_area
                