class Solution(object):
    def isValid(self, s):
        stack = []
        
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char) 
            elif char == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif char == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            elif char == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
        """
        :type s: str
        :rtype: bool
        """
        