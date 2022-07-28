# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/24 16:20
@Auth ： Gancheng Yuan

leetcode #2
"""
from leetcodeutils.misc import ListNode

from leetcodeutils.base import CaseWrapper
from leetcodeutils.core import CaseExecutor


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        head = curr = ListNode()
        carry = val = 0

        while carry or l1 or l2:
            val = carry

            if l1: l1, val = l1.next, l1.val + val
            if l2: l2, val = l2.next, l2.val + val

            carry, val = divmod(val, 10)
            curr.next = curr = ListNode(val)

        return head.next


if __name__ == '__main__':
    # define a wrapper for test case
    case_wrapper = CaseWrapper(
        [2, 4, 3],
        [5, 6, 4]
    )

    # define a test case executor which can execute user's indicated method
    case_executor = CaseExecutor(
        target_class=Solution,
        target_method_name="addTwoNumbers",
        case=case_wrapper
    )

    # invoke execute() method to run user's indicated method and get result
    converted_output = case_executor.execute()
    print("output of running testcase is {}".format(converted_output))
