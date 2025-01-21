class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res= 0
        for i in range(32):
            if (n>>i)&1:
                res+=1
        return res

#        while(i < 32):  # Loop over each bit position (0 to 31)
#             if (1 << i) & n != 0:  # Check if the ith bit in n is 1
#                 count += 1  # If the ith bit is 1, increment count
#             i += 1  # Move to the next bit