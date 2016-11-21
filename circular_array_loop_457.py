class Solution(object):

    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        seen = [False for i in range(N)]

        for i in range(N):
            if not seen[i]:
                seen[i] = True
                sign = nums[i] > 0
                start = i
                cur = i
                length = 1

                while ((nums[(cur + nums[cur]) % N] > 0) == (nums[start] > 0)):
                    cur = (cur + nums[cur]) % N

                    if length > 1 and cur == start:
                        return True
                    elif seen[cur]:
                        break

                    seen[cur] = True
                    length += 1

        return False
