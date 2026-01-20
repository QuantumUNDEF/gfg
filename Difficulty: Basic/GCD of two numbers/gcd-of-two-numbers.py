class Solution:
    def gcd(self, a, b):
        # code here
        while(a%b!=0):
            rem = a%b
            a = b
            b = rem
        return b