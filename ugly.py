# Govinda KC
# Date modified 11/27/2018
# Extra credit problem
# finding the Ugly Number.


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initializtion
        ugly_list = [1]
        # Track of the index
        index_2 = 0
        index_3 = 0
        index_5 = 0
        while len(ugly_list) < n:
            next_ugly = min(ugly_list[index_2] * 2, ugly_list[index_3] * 3, ugly_list[index_5] * 5)
            # Move the index of the minimum
            if next_ugly == ugly_list[index_2] * 2:
                index_2 += 1
            if next_ugly == ugly_list[index_3] * 3:
                index_3 += 1
            if next_ugly == ugly_list[index_5] * 5:
                index_5 += 1
            ugly_list.append(next_ugly)
        return ugly_list[len(ugly_list) - 1]

ob = Solution()
n = 7
print("The", n, "ugly number", ob.nthUglyNumber(n))
