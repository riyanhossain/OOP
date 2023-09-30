class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        eNums = sorted(list(set(nums)))
        for i in range(len(eNums)):
            nums[i] = eNums[i]
        return len(eNums)


solution = Solution()

print(
    solution.removeDuplicates(
        [
            1,
            1,
            2,
        ]
    )
)
