class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            # 如果是右括號，且 stack 空了或者不匹配
            elif not stack or stack.pop() != char:
                return False
        return not stack