class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        i = 0
        j = 0
        idx = -1
        while i < len(txt) and j< len(pat):
            if(txt[i] == pat[j]):
                i+=1
                j+=1
                if(j == len(pat)):
                    idx = i-j 
                    break
            else:
                i = i-j+1
                j = 0
            
        return idx
                