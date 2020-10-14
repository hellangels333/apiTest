# coding=utf-8

import pytest
import os
import glob


# 查找所有待执行的测试用例module，见《04|必知必会，打好Python基本功》
def find_modules_from_folder(folder):
    absolute_f = os.path.abspath(folder)
    md = glob.glob(os.path.join(absolute_f, "*.py"))
    return [f for f in md if os.path.isfile(f) and not f.endswith('__init__.py')]

if __name__ == "__main__":
    # 得出测试文件夹地址
    test_folder = os.path.join(os.path.dirname(__file__), 'tests')  # 只扫描tests文件夹下的
    # 得出测试文件夹下的所有测试用例
    target_file = find_modules_from_folder(test_folder)
    # 直接运行所有的测试用例
    pytest.main([*target_file, '-v'])

    # 运行标记“smoke”的用例;用allure输出测试报告;如有错误，错误的执行2次(重复1次);多进程最多2个进程一起执行；每个进程最多3个线程一起执行
    # pytest.main(["-m", "smoke", "--alluredir=./allure_reports", "--reruns 2", "workers 2", "test-per-worker 3"])


