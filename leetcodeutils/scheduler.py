# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/27 0:51
@Auth ： Gancheng Yuan
"""
from abc import ABCMeta, abstractmethod

from leetcodeutils.base import CaseWrapper
from leetcodeutils.utils import CommonUtils, CommonParamsResolver


class CaseScheduler(metaclass=ABCMeta):

    @abstractmethod
    def schedule(self):
        return NotImplemented


class CommonCaseScheduler(CaseScheduler):

    def __init__(self, target_class, target_method_name, case: CaseWrapper):
        self.target_class = target_class
        self.target_method_name = target_method_name
        self.param_list = case.get_params()

    def schedule(self):
        target_instance = self.target_class()
        target_params_list = CommonParamsResolver.resolve(self.target_class, target_instance, self.target_method_name, self.param_list)
        target_function = target_instance.__getattribute__(self.target_method_name)
        return target_function(*target_params_list)


class ComplexCaseScheduler(CaseScheduler):

    def __init__(self, target_class, case: CaseWrapper):
        self.target_class = target_class
        self.all_invoke_list = case[0]
        self.all_invoke_params_list = case[1]

    def schedule(self):
        if len(self.all_invoke_list) == 0:
            return []
        target_class_instance = None
        target_result_list = []
        for i in range(0, len(self.all_invoke_list)):
            invoke_str = self.all_invoke_list[i]
            if invoke_str == self.target_class.__name__:
                target_class_instance = CommonUtils.get_class_instance_by_init_params(self.target_class, self.all_invoke_params_list[i])
                target_result = None
            else:
                resolved_param_list = CommonParamsResolver.resolve(self.target_class, target_class_instance, invoke_str, self.all_invoke_params_list[i])
                target_method = target_class_instance.__getattribute__(invoke_str)
                if len(resolved_param_list) == 0:
                    target_result = target_method()
                else:
                    target_result = target_method(*resolved_param_list)
            target_result_list.append(target_result)
        return target_result_list
