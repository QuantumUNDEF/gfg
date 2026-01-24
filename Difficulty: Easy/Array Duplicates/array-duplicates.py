class Solution:
    def findDuplicates(self, arr):
        # code here
        dct = {}
        n = len(arr)
        for i in range(n):
            if arr[i] not in dct:
                dct[arr[i]] = 1
            else:
                dct[arr[i]] += 1
        return [ i for i in dct if dct[i] >= 2]
                
        
            
        