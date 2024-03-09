#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        
        for i in range(r):
            tmp=""
            for num in s:
                if num == "1":
                  tmp+="10"  
                else:
                    tmp+="01"
            tmp=tmp[:n+1]
            s=tmp
            
        
        return s[n]





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends