class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        opening_brackets = "({["

        for ch in s:
            if ch in opening_brackets:
                stack.append(ch)
            else:
                # If stack is empty, no matching open bracket
                if not stack:
                    return False
                # Check matching brackets
                if ch == ')' and stack[-1] == '(':
                    stack.pop()
                elif ch == '}' and stack[-1] == '{':
                    stack.pop()
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        # Stack must be empty for valid string
        return not stack
            
