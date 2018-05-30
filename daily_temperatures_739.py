class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st = []
        result = [0 for i in range(len(temperatures))]

        for i, t in enumerate(temperatures):
            if not st:
                st.append((t, 0))
            else:
                while st and t > st[-1][0]:
                    _, idx = st.pop()
                    result[idx] = i - idx
                st.append((t, i))

        return result
