class Solution:
    def checkStatus(self, a, b, flag):
        if (flag == False and ((a >= 0) ^ (b >= 0))) or (flag == True and (a < 0 and b < 0)) : 
            return True
        else:
            return False