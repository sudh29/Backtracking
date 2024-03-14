class Solution:
    def allPalindromicPerms(self, S):
        self.res = set()
        self.solve(list(S))
        return sorted(list(self.res))
        
    def solve(self,arr):
        self.res.add(tuple(arr))
        if len(arr)<=1:
            return
        for i in range(1,len(arr)):
            if arr[i-1]==arr[i]:
                new_arr = arr[:i-1]+ [arr[i-1]+arr[i]] + arr[i+1:]
                self.solve(new_arr)
            if i+1< len(arr) and arr[i-1]==arr[i+1]:
                new_arr = arr[:i-1]+ [arr[i-1]+arr[i]+arr[i+1]] + arr[i+2:]
                self.solve(new_arr)
