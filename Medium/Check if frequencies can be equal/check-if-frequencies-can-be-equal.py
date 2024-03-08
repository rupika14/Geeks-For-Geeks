#User function Template for python3
class Solution:
    def sameFreq(self, s):
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
    
        unique_counts = set(count.values())
        if len(unique_counts) == 1 or (len(unique_counts) == 2 and 1 in unique_counts):
            return True
    
        for char in count:
            temp_count = count.copy()
            temp_count[char] -= 1
            if len(set(temp_count.values())) == 1:
                return True
    
        return False
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends