class Solution(object):

    def combinationSum2(self, candidates, target):
        ans = []
        self.search(0, sorted(candidates), [], ans, target, 0)
        return ans

    def search(self, start, nums, cur, ans, target, sum):
        if sum > target:
            return

        if sum == target:
            ans.append(cur[:])
            return

        for i in range(start, len(nums)):
            if start != i and nums[i] == nums[i - 1]:
                continue

            cur.append(nums[i])
            self.search(i + 1, nums, cur, ans, target, sum + nums[i])
            cur.pop()
