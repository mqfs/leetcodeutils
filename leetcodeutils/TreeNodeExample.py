# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/24 16:20
@Auth ： Gancheng Yuan

leetcode #226
"""
from leetcodeutils.misc import TreeNode

from leetcodeutils.base import CaseWrapper
from leetcodeutils.core import CaseExecutor


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root


if __name__ == '__main__':
    # define a wrapper for test case
    case_wrapper = CaseWrapper(
        [4,2,7,1,3,6,9]
    )

    # define a test case executor which can execute user's indicated method
    case_executor = CaseExecutor(
        target_class=Solution,
        target_method_name="invertTree",
        case=case_wrapper
    )

    # invoke execute() method to run user's indicated method and get result
    converted_output = case_executor.execute()
    print("output of running testcase is {}".format(converted_output))
