import hw2_for_task1 as hw2
import hw3_for_task1 as hw3
import hw4_for_task1 as hw4

from inspect import getmembers, isfunction


func_list_hw2 = [o[0] for o in getmembers(hw2) if isfunction(o[1])]
func_list_hw3 = [o[0] for o in getmembers(hw3) if isfunction(o[1])]
func_list_hw4 = [o[0] for o in getmembers(hw4) if isfunction(o[1])]
all_func_list = [func_list_hw2, func_list_hw3, func_list_hw4]


def runner(*args):
    if not len(args):
        for func in func_list_hw2:
            call_def = getattr(hw2, func)
            call_def()
        for func in func_list_hw3:
            call_def = getattr(hw3, func)
            call_def()
        for func in func_list_hw4:
            call_def = getattr(hw4, func)
            call_def()
    elif len(args) != 0:
        for callable_func in args:
            if callable_func in func_list_hw2:
                call_def = getattr(hw2, callable_func)
                call_def()
            elif callable_func in func_list_hw3:
                call_def = getattr(hw3, callable_func)
                call_def()
            elif callable_func in func_list_hw4:
                call_def = getattr(hw4, callable_func)
                call_def()


runner()
runner('task1_hw4')
runner('task1_hw4', 'task2_hw4', 'task3_hw2')
