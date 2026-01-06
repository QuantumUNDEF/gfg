class Solution:
    def majorityElement(self, arr):
        # code here
        n = len(arr)//2
        arr.sort()
        dct = {}
        for i in range(len(arr)):
            if arr[i] in dct:
                dct[arr[i]] += 1
            else:
                dct[arr[i]] = 1
        for i in dct:
            if dct[i] > n:
                return i
        else:
            return -1