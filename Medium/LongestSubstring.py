# Concept used: Sliding window
# Program is well documented.
# Summary: Use a sliding window. Maintain a unique set along with sliding window to keep track of characters so that they should not repeat.
# Idea is to

# Slide the window right-ward till repetition does not occur.
# Update the max size of window (our output)
# Slide the window from left i.e. omit the left-most character. (Remove it from unique set as well)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0                 #Start or left pointer of sliding window
        end=0                   #End or right pointer of sliding window
        maxWindow=0             #To find the max size of window
        uniqueSet=set()         #To maintain that no characters are repeated in a set
        while start<=end and end<len(s):
            while end<len(s) and s[end] not in uniqueSet:
                uniqueSet.add(s[end])               #Shift window right-ward till no repetition
                end+=1
            maxWindow=max(maxWindow,len(uniqueSet)) #Update the max window after checking size of current window
            uniqueSet.remove(s[start])              #Move the window by one character from left | 
                                                    #Don't forget to remove the character from unique set as well
            start+=1
        return maxWindow