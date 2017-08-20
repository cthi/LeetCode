class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def parseInt(y):
            if y[0] == '-':
                return -1 * int(y[1:])
            else:
                return int(y)

        y, u = a.split('+')
        i, o = b.split('+')

        u = u[:len(u) - 1]
        o = o[:len(o) - 1]

        y = parseInt(y)
        u = parseInt(u)
        i = parseInt(i)
        o = parseInt(o)

        yi = y * i
        yo = y * o
        ui = u * i
        uo = u * o

        return str(yi - uo) + "+" + str(yo + ui) + "i"
