# iTesting.py
# coding=utf-8
import pytest
class TestSample(object):
    # 测试用例默认以test开头
    def test_equal(self):
        assert 1 == 1
    def test_not_equal(self):
        assert 1 != 0

# 文件名tests/test_sample.py  pytest框架能兼容unittest的测试用例
# coding=utf-8
import unittest
#测试类必须要继承TestCase类
class TestSample2(unittest.TestCase):
    #测试用例默认以test开头
    def test_equal(self):
        self.assertEqual(1, 1)
    def test_not_equal(self):
        self.assertNotEqual(1, 0)
if __name__ == '__main__':
    unittest.main()