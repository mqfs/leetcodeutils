# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/24 16:20
@Auth ： Gancheng Yuan
"""
from typing import List

from leetcodeutils import CaseWrapper, CaseExecutor


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], i]
            dic[nums[i]] = i
        return []


if __name__ == '__main__':
    # define a wrapper for test case
    case_wrapper = CaseWrapper(
        [2, 7, 11, 15],
        9
    )

    # define a test case executor which can execute user's indicated method
    case_executor = CaseExecutor(
        target_class=Solution,
        target_method_name="twoSum",
        case=case_wrapper
    )

    # invoke execute() method to run user's indicated method and get result
    returned_value = case_executor.execute()
    print("returned value with running user's indicated method is {}".format(returned_value))
