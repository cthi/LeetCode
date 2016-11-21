class Solution(object):

    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if not self.isOp(token):
                stack.append(token)
            else:
                op = token
                r = stack.pop()
                l = stack.pop()
                stack.append(str(self.eval(l, r, op)))

        return int(stack[-1])

    def isOp(self, token):
        return token == '+' or token == '-' or token == '*' or token == '/'

    def eval(self, l, r, op):
        print(l, r, op)
        l = int(l)
        r = int(r)

        if op == '+':
            return l + r
        elif op == '-':
            return l - r
        elif op == '*':
            return l * r
        else:
            if l * r < 0:
                return - (abs(l) // abs(r))
            else:
                return l // r
