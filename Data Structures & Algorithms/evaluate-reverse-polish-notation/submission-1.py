class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = []

        for token in tokens:
            
            if token not in ['+','-','*','/']:
                temp.append(int(token))

            else:
                b = temp.pop()
                a = temp.pop()
                if token == '+':
                    temp.append(a+b)
                elif token == '-':
                    temp.append(a-b)
                elif token == '*':
                    temp.append(a*b)
                else:
                    temp.append(int(a / b))
        
        return temp[0]
                