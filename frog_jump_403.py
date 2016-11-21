class Solution(object):

    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[0] != 0 or stones[1] != 1:
            return False

        return self.canCrossHelper(1, 1, stones[-1], set(stones), {})

    def canCrossHelper(self, curStone, lastJump, goal, stones, memo):
        if curStone == goal:
            return True
        elif (curStone, lastJump) in memo:
            return memo[(curStone, lastJump)]
        elif curStone not in stones:
            return False
        else:
            res = self.canCrossHelper(
                curStone + lastJump + 1, lastJump + 1, goal, stones, memo)
            res = res or self.canCrossHelper(
                curStone + lastJump, lastJump, goal, stones, memo)
            if lastJump != 1:
                res = res or self.canCrossHelper(
                    curStone + lastJump - 1, lastJump - 1, goal, stones, memo)

            memo[(curStone, lastJump)] = res
            return res
