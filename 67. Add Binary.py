class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = int(a,2)
        y= int(b,2)
        return bin(x+y)[2:]

        #or 

        # x=len(a)-1
        # y=len(b)-1
        # carry=0

        # result = ""

        # while x>=0 or y>=0 or carry:
        #     bit_a = int(a[x]) if x >= 0 else 0
        #     bit_b = int(b[y]) if y>=0 else 0

        #     sum_bits = bit_a + bit_b + carry
        #     result += str(sum_bits%2)
        #     carry= sum_bits//2

        #     x -= 1
        #     y -= 1

        # return result[::-1]
