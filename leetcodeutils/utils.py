# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/28 11:27
@Auth ： Gancheng Yuan
"""
import re
from inspect import signature

from leetcodeutils.misc import ListNode, null, TreeNode, true, false

from leetcodeutils.base import CaseWrapper


class CommonUtils:

    @staticmethod
    def get_class_instance_by_case(target_class, case: CaseWrapper):
        if CommonUtils.is_target_class_name_exists_in_case(target_class.__name__, case):
            init_param_list = case[1][0]
            return CommonUtils.get_class_instance_by_init_params(target_class, init_param_list)
        else:
            return CommonUtils.get_class_instance_by_init_params(target_class, [])

    @staticmethod
    def get_class_instance_by_init_params(target_class, init_param_list: list):
        resolved_param_list = CommonParamsResolver.resolve(target_class, None, '__init__', init_param_list)
        if len(resolved_param_list) == 0:
            target_class_instance = target_class()
        else:
            target_class_instance = target_class(*resolved_param_list)
        return target_class_instance

    @staticmethod
    def get_method_signature(target_class, target_class_instance, target_method_name):
        if target_method_name is None or target_method_name == '' or target_method_name == '__init__':
            target_method = target_class.__init__
        else:
            target_method = target_class_instance.__getattribute__(target_method_name)
        return signature(target_method)

    @staticmethod
    def is_target_class_name_exists_in_case(target_class_name: str, case: CaseWrapper) -> bool:
        if len(case) == 0:
            return False
        first = case[0]
        if not isinstance(first, list) or len(first) == 0:
            return False
        else:
            first_element = first[0]
            if isinstance(first_element, str) and first_element == target_class_name:
                return True
            else:
                return False

    @staticmethod
    def convert_result_to_output(result):
        if result is None:
            return null()
        elif isinstance(result, bool):
            return CommonUtils.convert_bool_to_output(result)
        elif isinstance(result, list):
            return CommonUtils.convert_list_to_output(result)
        elif isinstance(result, ListNode):
            return CommonUtils.convert_list_node_to_output(result)
        elif isinstance(result, TreeNode):
            return CommonUtils.convert_tree_node_to_output(result)
        else:
            return result

    @staticmethod
    def convert_bool_to_output(bool_result):
        if bool_result:
            return true()
        else:
            return false()

    @staticmethod
    def convert_list_to_output(list_result):
        converted_result = []
        for item in list_result:
            converted_item = CommonUtils.convert_result_to_output(item)
            converted_result.append(converted_item)
        return converted_result

    @staticmethod
    def convert_list_node_to_output(list_node_result):
        converted_result = []
        node = list_node_result
        while node is not None:
            converted_result.append(node.val)
            node = node.next
        return converted_result

    @staticmethod
    def convert_tree_node_to_output(tree_node_result):
        converted_result = []
        root = tree_node_result
        temp_tree_node_queue = [root]
        while len(temp_tree_node_queue) > 0:
            cur_size = len(temp_tree_node_queue)
            for i in range(0, cur_size):
                if temp_tree_node_queue[i] is None:
                    converted_result.append(null())
                else:
                    converted_result.append(temp_tree_node_queue[i].val)
                    temp_tree_node_queue.append(temp_tree_node_queue[i].left)
                    temp_tree_node_queue.append(temp_tree_node_queue[i].right)
            for i in range(0, cur_size):
                temp_tree_node_queue.pop(0)
        while len(converted_result) > 0 and (converted_result[-1] is None or isinstance(converted_result[-1], null)):
            converted_result.pop()
        return converted_result


class CommonParamsResolver:

    @staticmethod
    def resolve(target_class, target_class_instance, target_method_name: str, param_list: list) -> list:
        if len(param_list) == 0:
            return []
        method_signature = CommonUtils.get_method_signature(target_class, target_class_instance, target_method_name)
        resolved_param_list = []
        i = 0
        for param_name in method_signature.parameters:
            if param_name == 'self':
                continue
            param = param_list[i]
            param_type_str = CommonParamsResolver.get_type_str(method_signature.parameters[param_name].annotation)
            target_param = CommonParamsResolver.get_customized_param(param, param_type_str)
            resolved_param_list.append(target_param)
            i += 1
        return resolved_param_list

    @staticmethod
    def get_type_str(orig_type) -> str:
        orig_type_str = str(orig_type)
        union_type_reg = re.search("typing\\.Union.*", orig_type_str)
        if union_type_reg is not None:
            union_inner_str = orig_type_str[13:-1]
            type_str = union_inner_str.split(',')[0].split('.')[-1]
        else:
            not_union_type_reg = re.search("typing\\..*", orig_type_str)
            if not_union_type_reg is not None:
                type_str = orig_type_str
            else:
                type_str_start, type_str_open_end = re.search("'.*'", orig_type_str).span()
                qualified_type_str = orig_type_str[type_str_start + 1:type_str_open_end - 1]
                if '.' in qualified_type_str:
                    type_str = qualified_type_str.split('.')[-1]
                else:
                    type_str = qualified_type_str
        return type_str

    @staticmethod
    def get_customized_param(param, customized_type_name: str):
        result_param = param
        if customized_type_name == 'ListNode':
            virtual_head = ListNode()
            node = virtual_head
            for val in param:
                if val == null:
                    list_node = None
                else:
                    list_node = ListNode(val)
                node.next = list_node
                if node.next is None:
                    break
                node = node.next
            result_param = virtual_head.next
        elif customized_type_name == 'TreeNode':
            tree_size = len(param)
            if tree_size > 0:
                root = TreeNode(param[0])
                temp_queue_1 = [root]
                i = 1
                while i < tree_size:
                    temp_queue_2 = []
                    for node in temp_queue_1:
                        if node is None:
                            continue
                        if i >= tree_size or param[i] == null:
                            left_child = None
                        else:
                            left_child = TreeNode(param[i])
                        if i + 1 >= tree_size or param[i + 1] == null:
                            right_child = None
                        else:
                            right_child = TreeNode(param[i + 1])
                        node.left = left_child
                        node.right = right_child
                        temp_queue_2.append(left_child)
                        temp_queue_2.append(right_child)
                        i += 2
                    temp_queue_1 = temp_queue_2.copy()
                result_param = root
            else:
                result_param = None
        return result_param
