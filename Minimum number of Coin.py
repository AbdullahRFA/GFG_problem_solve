class Solution:
    def findMin(self, n):
       # code here 
       coin = [10,5,2,1]
       cnt = 0
       
       for i in coin:
           if n>=i:
               c = n//i
               cnt += c
               n-=(c*i)
        
       return cnt
           
       