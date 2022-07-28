# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/24 14:51
@Auth ： Gancheng Yuan
"""
from leetcodeutils.base import CaseWrapper
from leetcodeutils.misc import null
from leetcodeutils.scheduler import CommonCaseScheduler, ComplexCaseScheduler
from leetcodeutils.utils import CommonUtils, CommonParamsResolver


class CaseExecutor:

    def __init__(self, target_class, case: CaseWrapper, target_method_name=None):
        self.target_class = target_class
        self.case_wrapper = case
        self.target_method_name = target_method_name

    def execute(self):
        result_of_case = CaseSchedulerDispatcher.dispatch(self.target_class, self.target_method_name, self.case_wrapper)
        return self.__convert_result_of_case_to_output(result_of_case)

    def __convert_result_of_case_to_output(self, result_of_case):
        target_class_instance = CommonUtils.get_class_instance_by_case(self.target_class, self.case_wrapper)
        method_sig = CommonUtils.get_method_signature(self.target_class, target_class_instance, self.target_method_name)
        if method_sig.return_annotation is None:
            return_type_str = ''
        else:
            return_type_str = CommonParamsResolver.get_type_str(method_sig.return_annotation)
        if result_of_case is None:
            if return_type_str == 'TreeNode' or return_type_str == 'ListNode':
                return []
            else:
                return null()
        else:
            return CommonUtils.convert_result_to_output(result_of_case)


class CaseSchedulerDispatcher:

    @staticmethod
    def dispatch(target_class, target_method_name, case: CaseWrapper):
        if CommonUtils.is_target_class_name_exists_in_case(target_class.__name__, case):
            complex_case_scheduler = ComplexCaseScheduler(target_class, case)
            return complex_case_scheduler.schedule()
        else:
            common_case_scheduler = CommonCaseScheduler(target_class, target_method_name, case)
            return common_case_scheduler.schedule()

