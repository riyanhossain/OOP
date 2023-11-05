class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        outputStr = ""
        sortedList = sorted(strs)
        first = sortedList[0]
        last = sortedList[-1]
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                outputStr = outputStr + first[i]
            else:
                break

        return outputStr


def main():
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))


main()
