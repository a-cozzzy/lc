class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = s.split()
        stack.reverse()
        return ' '.join(stack)