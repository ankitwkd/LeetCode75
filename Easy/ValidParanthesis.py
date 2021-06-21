class Solution:
    def isValid(self, s: str) -> bool:
        #Maintain a stack to 1) Push open brackets 2) Pop open brackets when close brackets arrive
        stack = []
        
        #Maintain a map from opening brackets to corresponding closing bracket
        m = {'(':')', '{':'}','[':']'}
        
        #Iterate each bracket in input string
        for i in s:
            #If it is open bracket, then push to stack.
            if i in ('(','{','['):
                stack.append(i)
            #If it is close bracket, then analyse the topmost element of stack
            else:
                #EDGE-CASE: If it is close bracket, but stack is empty then it's invalid, return False
                if not stack:
                    return False
                #Otherwise pop the top-most bracket and check if it's corresponding open bracket or not
                b = stack.pop()
                if i != m[b]:                   #If any one bracket mismatches, return False
                    return False
        
        
        #Edge-case: What if stack is still not empty? return False
        if len(stack) > 0:
            return False
        return True