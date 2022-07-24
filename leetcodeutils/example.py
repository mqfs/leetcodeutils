# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/24 16:20
@Auth ： Gancheng Yuan
"""
from typing import Optional

from leetcodeutils import CaseWrapper, CaseExecutor


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = l1, l2
        ans = cur = ListNode()
        carry = 0

        while node1 or node2:
            if node1 and node2:
                v = node1.val + node2.val + carry
                node1 = node1.next
                node2 = node2.next
            elif node1 is None:
                v = node2.val + carry
                node2 = node2.next
            else:
                v = node1.val + carry
                node1 = node1.next

            carry, v = divmod(v, 10)
            cur.next = ListNode(v)
            cur = cur.next

        if carry:
            cur.next = ListNode(1)
        ans = ans.next

        return ans


if __name__ == '__main__':
    # define a wrapper for test case
    case_wrapper = CaseWrapper(
        [2,4,3],
        [5,6,4]
    )

    # define a test case executor which can execute user's indicated method
    case_executor = CaseExecutor(
        target_class=Solution,
        target_method_name="addTwoNumbers",
        case=case_wrapper
    )

    # invoke execute() method to run user's indicated method and get result
    returned_value = case_executor.execute()
    print("returned value with running user's indicated method is {}".format(returned_value))
