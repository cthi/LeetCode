class Solution(object):

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(reversed(s))
        decoded = ""
        stack = []

        while s:
            next = s.pop()

            if next.isdigit():
                while s[-1].isdigit():
                    next += s.pop()
                stack.append(next)
                stack.append(s.pop())  # [
            elif next == ']':
                tmp = []

                while stack[-1] != '[':
                    tmp.append(stack.pop())
                stack.pop()  # [
                times = int(stack.pop())
                stack.append(times * "".join(reversed(tmp)))
            else:
                while s and s[-1].isalpha():
                    next += s.pop()

                stack.append(next)

        return "".join(stack)
