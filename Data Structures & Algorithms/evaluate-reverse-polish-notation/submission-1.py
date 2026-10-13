class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {'+', '-', '*', '/'}
        stack = []
        for e in tokens:
            if e not in operands:
                stack.append(e)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if e == '+':
                    res_op = first + second
                elif e == '-':
                    res_op = first - second
                elif e == '*':
                    res_op = first * second
                else :
                    res_op = int(first/second)
                stack.append(res_op)
        return int(stack[0])