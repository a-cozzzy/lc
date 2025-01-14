class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ")}]":
                if not stack:
                    return False
                top = stack[-1]
                if top == '(' and char ==')':
                    stack.pop()
                elif top == '{' and char =='}':
                    stack.pop()
                elif top == '[' and char ==']':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0