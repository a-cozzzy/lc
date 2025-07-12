class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for t in tokens:
            # If the token is a number, push it to the stack
            if t.lstrip('-').isdigit():  # Handles negative numbers
                stack.append(int(t))
            else:
                # Pop two operands from the stack
                x = stack.pop()
                y = stack.pop()
                
                # Perform the operation based on the operator
                if t == '+':
                    z = y + x
                elif t == '-':
                    z = y - x
                elif t == '*':
                    z = y * x
                elif t == '/':
                    # Handle integer division and truncation towards zero
                    z = int(float(y) / x)  # Convert to int to ensure truncation towards zero
                else:
                    continue
                
                # Push the result back to the stack
                stack.append(z)
        
        # The result will be the only element in the stack
        return stack.pop()
 