# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/27 17:36
@Auth ： Gancheng Yuan
"""


class CaseWrapper:

    def __init__(self, *args):
        self.params = list(args)

    def get_params(self):
        return self.params

    def __getitem__(self, index):
        return self.params[index]

    def __len__(self):
        return len(self.params)
