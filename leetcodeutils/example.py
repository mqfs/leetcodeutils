# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/24 16:20
@Auth ： Gancheng Yuan
"""
from typing import Optional

from leetcodeutils import CaseWrapper, CaseExecutor
from leetcodeutils.misc import null, TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True


if __name__ == '__main__':
    # define a wrapper for test case
    case_wrapper = CaseWrapper(
        [5,1,4,null,null,3,6]
    )

    # define a test case executor which can execute user's indicated method
    case_executor = CaseExecutor(
        target_class=Solution,
        target_method_name="isValidBST",
        case=case_wrapper
    )

    # invoke execute() method to run user's indicated method and get result
    returned_value = case_executor.execute()
    print("returned value with running user's indicated method is {}".format(returned_value))
