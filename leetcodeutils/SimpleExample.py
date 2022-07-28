# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/24 16:20
@Auth ： Gancheng Yuan

leetcode #5
"""
from leetcodeutils.base import CaseWrapper
from leetcodeutils.core import CaseExecutor


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for L in range(2, n + 1):
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]


if __name__ == '__main__':
    # define a wrapper for test case
    case_wrapper = CaseWrapper(
        "babad"
    )

    # define a test case executor which can execute user's indicated method
    case_executor = CaseExecutor(
        target_class=Solution,
        target_method_name="longestPalindrome",
        case=case_wrapper
    )

    # invoke execute() method to run user's indicated method and get result
    converted_output = case_executor.execute()
    print("output of running testcase is {}".format(converted_output))
