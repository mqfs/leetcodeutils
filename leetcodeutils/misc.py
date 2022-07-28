# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/25 1:09
@Auth ： Gancheng Yuan
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class null:

    def __repr__(self):
        return "null"


class true:

    def __repr__(self):
        return "true"


class false:

    def __repr__(self):
        return "false"
