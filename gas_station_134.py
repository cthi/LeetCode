ass Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost) > sum(gas):
            return -1

        N = len(gas)
        i = 0
        seen = 0
        tank = 0
        ans = 0

        while seen < N:
            tank += gas[i]
            tank -= cost[i]

            i += 1
            seen += 1

            if tank < 0:
                tank = 0
                seen = 0
                ans = i

            if i == N:
                i = 0

        return ans
