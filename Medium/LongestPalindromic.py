# I found this approach simpler and easier to understand for people dreading the DP approach. So take a look.
# Approach: From centre expand outward till you find longest substring for each of the characters in the string.

# Traverse the whole string once and for each character, consider it as the centre of palindrome string and expand the window outward.
# Continue expanding outward till the substring is palindrome.
# Update the max length of palindrome strings found till now and the result as well.
# P.S: In order to handle even length substrings, we need to consider 2 characters at once to be the centre and then expand outward.

class Solution:
    def longestPalindrome(self, s: str) -> str:
#         #Brute force
#         max_len = 0
#         res = ''
#         for i in range(len(s)):
#             for j in range(i + 1, len(s)):
#                 curr = s[i:j+1]
#                 if curr == curr[::-1]:
#                     if len(curr)>max_len:
#                         res = curr
#                         max_len = len(curr)
                        
#         if res=='':
#             return s[0]
#         return res


        #Expand from center (outward)
        res = ''                        #
        max_len = 0
        
        for i in range(len(s)):         #Traverse the whole string O(n)
            
            
            #odd length substrings
            l, r = i, i                 #Fix the left and right pointers to current index    
            while l >= 0 and r < len(s) and s[l] == s[r]:   #Till the substring is palindrome, expand outward
                curr_len = r - l + 1
                if curr_len > max_len:      #If length of current palindrome string is bigger than past strings, update the max length and result
                    res = s[l:r + 1]
                    max_len = curr_len
                l -= 1                      #Expand outward
                r += 1
                
            #Repeat the same for even length substrings!!
            
            #even length substrings     
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > max_len:
                    res = s[l:r + 1]
                    max_len = curr_len
                l -= 1
                r += 1
            
        return res