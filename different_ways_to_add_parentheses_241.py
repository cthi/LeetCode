import re


class Solution(object):

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        input = re.split(r'(\+|\-|\*)', input)
        memo = {}
        return self.compute(input, memo)

    def compute(self, input, memo):
        inputAsStr = str(input)
        if inputAsStr in memo:
            return memo[inputAsStr]
        elif len(input) == 1:
            input[0] = int(input[0])
            return input
        else:
            solutions = []

            for i in range(len(input)):
                if input[i] == '+' or input[i] == '-' or input[i] == '*':
                    left = self.compute(input[0:i], memo)
                    right = self.compute(input[i + 1:], memo)
                    op = input[i]

                    if op == '+':
                        opFunc = lambda x, y: x + y
                    elif op == '-':
                        opFunc = lambda x, y: x - y
                    else:
                        opFunc = lambda x, y: x * y

                    for k in left:
                        for j in right:
                            solutions.append(opFunc(k, j))

            memo[inputAsStr] = solutions
            return solutions
