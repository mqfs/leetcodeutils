# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/24 14:51
@Auth ： Gancheng Yuan
"""
from inspect import signature
import re

from leetcodeutils.misc import ListNode


class CaseWrapper:

    def __init__(self, *args):
        self.params = list(args)

    def __getitem__(self, index):
        return self.params[index]


class CaseExecutor:

    def __init__(self, *target_class_init_args, target_class, target_method_name, case: CaseWrapper):
        self.target_class_init_args = target_class_init_args
        self.target_class = target_class
        self.target_method_name = target_method_name
        self.case_wrapper = case

    def execute(self):
        if self.target_class_init_args:
            target_instance = self.target_class(self.target_class_init_args)
        else:
            target_instance = self.target_class()
        target_params_list = CaseResolver.resolve(target_instance, self.target_method_name, self.case_wrapper)
        target_function = target_instance.__getattribute__(self.target_method_name)
        return target_function(*target_params_list)


class CaseResolver:

    @staticmethod
    def resolve(target_class_instance, target_method_name: str, case: CaseWrapper) -> list:
        target_method = target_class_instance.__getattribute__(target_method_name)
        method_signature = signature(target_method)
        resolved_param_list = list()
        i = 0
        for param_name in method_signature.parameters:
            param = case[i]
            param_type_str = CaseResolver.__get_type_str_of_method(method_signature.parameters[param_name].annotation)
            target_param = CaseResolver.__get_customized_param(param, param_type_str)
            resolved_param_list.append(target_param)
            i += 1
        return resolved_param_list

    @staticmethod
    def __get_type_str_of_method(orig_type) -> str:
        orig_type_str = str(orig_type)
        union_type_reg = re.search("typing\\.Union*", orig_type_str)
        if union_type_reg is not None:
            union_inner_str = orig_type_str[13:-1]
            type_str = union_inner_str.split(',')[0].split('.')[-1]
        else:
            not_union_type_reg = re.search("typing\\.*", orig_type_str)
            if not_union_type_reg is not None:
                type_str = orig_type_str
            else:
                type_str_start, type_str_open_end = re.search("'*'", orig_type_str).span()
                qualified_type_str = orig_type_str[type_str_start:type_str_open_end]
                if '.' in qualified_type_str:
                    type_str = qualified_type_str.split('.')[-1]
                else:
                    type_str = qualified_type_str
        return type_str

    @staticmethod
    def __get_customized_param(param, customized_type_name: str):
        result_param = param
        if customized_type_name == 'ListNode':
            virtual_head = ListNode()
            node = virtual_head
            for val in param:
                list_node = ListNode(val)
                node.next = list_node
                node = node.next
            result_param = virtual_head.next
        elif customized_type_name == 'TreeNode':
            # todo
            pass
        return result_param
