class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        tokens = self.tokenize(s)
        stack = self.parse(tokens, lambda x: x == '/' or x == '*')
        stack = self.parse(stack, lambda x: x == '+' or x == '-')

        return int(stack[0])

    def parse(self, tokens, isOp):
        stack = []

        for token in tokens:
            if stack and isOp(stack[-1]):
                op = stack.pop()
                left = stack.pop()
                right = token
                stack.append(str(self.compute(op, left, right)))
            else:
                stack.append(token)

        return stack

    def tokenize(self, s):
        tokens = []
        buf = ""

        for char in s:
            if char.isdigit():
                buf += char
            elif char.isspace():
                continue
            else:
                tokens.append(buf)
                tokens.append(char)
                buf = ""

        if buf:
            tokens.append(buf)

        return tokens

    def compute(self, c, l, r):
        l = int(l)
        r = int(r)
        if c == '+':
            return l + r
        elif c == '-':
            return l - r
        elif c == '*':
            return l * r
        else:
            return l / r
