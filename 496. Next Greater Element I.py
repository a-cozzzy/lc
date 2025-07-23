class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        nge = {}

        for num in nums2:

            while stack and num> stack[-1]:
                popped = stack.pop()
                nge[popped] = num

            stack.append(num)

        while stack:
            popped = stack.pop()
            nge[popped] = -1

        result = []
        for n1 in nums1:
            result.append(nge[n1]) 

        return result