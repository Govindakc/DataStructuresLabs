# Govinda KC
# Lab 5A
# Professor Aguirre, Diego
# TA Saha Manoj
# Date of last modification: 11/27/2018
# Extra credit problem: Finding the super ugly number

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # Initialization
        super_ugly = [1]
        # Dictionary to track index for each prime number
        prime_indices = {}

        # Initialize of dictionary
        for num in primes:
            prime_indices[num] = 0

        # Compute super ugly numbers.
        while len(super_ugly) < n:
            all_uglies = []
            # Compute and find the min of all super ugly numbers
            for num in prime_indices:
                all_uglies.append(num * super_ugly[prime_indices[num]])
            min_ugly = min(all_uglies)

            # Match the min ugly to its position and add 1 to its index
            for num in prime_indices:
                if min_ugly == num * super_ugly[prime_indices[num]]:
                    prime_indices[num] += 1
            # Add the super ugly number to the list
            super_ugly.append(min_ugly)

        # Return the last number(nth super ugly number))
        return super_ugly[len(super_ugly) - 1]

ob = Solution()
n = 5
primes = [3,7,8,11]
print("The", n, "super ugly number:", ob.nthSuperUglyNumber(n,primes))
