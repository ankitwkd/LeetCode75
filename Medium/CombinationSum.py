# Logic used: Choose candidate one by one.
# Once we choose a candidate, in order to move forward with combinations, we are considering 2 possible decisions:

# Include the current candidate in future combinations (Duplicate current candidate combined with others)
# Exclude the current candidate completely and look for combinations.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #Result list to be returned 
        res = []
        
        def dfs(index, curr, total):
            #Success case: If total is equal to target sum, append current set of candidates to result list
            if total == target:
                res.append(curr.copy())
                return
                
            #Failure case: If no candidates are left or total > target
            if index >= len(candidates) or total > target:
                return
            
            #Decision1: Include current candidate
            curr.append(candidates[index])
            dfs(index, curr, total + candidates[index])
            
            #Decision2: Exclude current candidate
            curr.pop()
            dfs(index + 1, curr, total)
            
        
        dfs(0, [], 0)
        return res