class Solution:
    def getAlternates(self, arr):
        return [arr[i] for i in range(0,len(arr),2)]