#User function Template for python3

class Solution:
    def count (self,s):
        l=u=sp=n=0
        # your code here
        for i in s:
            if i.islower():
                l+=1
            elif i.isupper():
                u+=1
            elif i.isnumeric():
                n+=1
            else:
                sp+=1
        return u,l,n,sp


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
# Contributed By: Pranay Bansal

# } Driver Code Ends