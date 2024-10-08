#User function Template for python3

class Solution:
    def prime_Sum(self, n):
        if n<=1:
            return 0

        # sieve of eratosthenes algo- Create a boolean array "prime[0..n]" and initialize
        # all entries it as true. A value in prime[i] will
        # finally be false if i is Not a prime, true if i is a prime
        prime = [True] * (n+1)
        
        prime[0] = False   # as 0 and 1 are nonprime numbers
        prime[1] = False
        
        # if the number is prime, mark its multiples as non-prime, false 
        i = 2
        while i*i<=n:
            if prime[i]:
                j = i*i
                while j<=n:
                    prime[j] = False  # Marking multiples of p as false indicating non-prime
                    j += i
            i += 1
            
        
        # Sum all prime numbers
        sum = 0
        for p in range(2, n+1):
            if prime[p]:
                sum += p

        return sum


# class Solution:
# 	def prime_Sum(self, n):
# 		# Code here
# 		def is_prime(num):
# 		    if num <= 1:
# 		        return 0
# 		    if num == 2 or num == 3:
# 		        return 1
# 		    if num % 2 == 0 or num % 3 == 0:
# 		        return 0
# 		    i = 5
# 		    while i * i <= num:
# 		        if num % i == 0 or num % (i+2) == 0:
# 		            return 0
# 		        i += 6
# 		    return 1
		    
# 		prime_sum = 0
# 		for i in range(2, n+1):
# 		    if is_prime(i):
# 		        prime_sum += i
		    
# 		return prime_sum
		            
		   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		ob = Solution()
		ans = ob.prime_Sum(n)
		print(ans)
# } Driver Code Ends