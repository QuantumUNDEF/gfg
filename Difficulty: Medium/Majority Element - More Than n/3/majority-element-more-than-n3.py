class Solution:
    def findMajority(self, arr):
        # code here
        arr.sort()
        n = len(arr)//3
        dct = {}
        l =[]
        for i in range(len(arr)):
            if arr[i] in dct:
                dct[arr[i]] += 1
            else:
                dct[arr[i]] = 1
        for i in (dct):
            if dct[i] > n:
                l.append(i)
        return l
            