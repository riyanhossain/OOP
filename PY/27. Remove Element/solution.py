class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        newNums = nums.copy()
        for num in newNums:
            if num == val:
                nums.remove(val)
        return len(nums)


def main():
    solution = Solution()
    print(solution.removeElement([3,2,2,3], 3))


main()
