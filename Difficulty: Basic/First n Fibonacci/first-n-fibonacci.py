#User function Template for python3

class Solution:
    def fibonacciNumbers(self, n):
        a = 0
        b = 1
        res = []

        for i in range(n):
            res.append(a)
            
            c = a + b
            a = b
            b = c
        
        return res