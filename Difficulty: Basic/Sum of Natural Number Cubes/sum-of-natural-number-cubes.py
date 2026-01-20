#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        #code here
        ans = 0
        for i in range(1, n+1):
            ans += i**3
        return ans