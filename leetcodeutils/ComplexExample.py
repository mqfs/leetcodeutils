# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/24 16:20
@Auth ： Gancheng Yuan

leetcode #173
"""
from leetcodeutils.misc import TreeNode, null

from leetcodeutils.base import CaseWrapper
from leetcodeutils.core import CaseExecutor


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.curr = root

    def next(self) -> int:
        while self.curr.left:
            left = self.curr.left
            while left.right and left.right != self.curr:
                left = left.right
            # left child has been visited
            if left.right:
                left.right = None
                break
            # left child has not been visited
            else:
                left.right = self.curr
                self.curr = self.curr.left
        # visit current node and go right
        ans = self.curr.val
        self.curr = self.curr.right
        return ans

    def hasNext(self) -> bool:
        return True if self.curr else False


if __name__ == '__main__':
    # define a wrapper for test case
    case_wrapper = CaseWrapper(
        ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
        [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
    )

    # define a test case executor which can execute user's indicated method
    case_executor = CaseExecutor(
        target_class=BSTIterator,
        target_method_name="",
        case=case_wrapper
    )

    # invoke execute() method to run user's indicated method and get result
    converted_output = case_executor.execute()
    print("output of running testcase is {}".format(converted_output))
