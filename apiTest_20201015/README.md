## 0.运行方式
1. 命令行运行 python -m pytest tests/test_ApiTest/test_lagou.py --html=report.html
2. 命令行运行 pytest tests/test_ApiTest/test_lagou.py --html=report.html
3. 有main.py直接 python main.py，格式参考上面（重难点是加各种参数）

## 1.pytest一些操作
1. 指定运行特定的方法,在命令行运行  pytest test_lagou.py::TestLaGou::test_get_new_message
2. 加标签（装饰器)，在run时跳过等
     @pytest.mark.smoke
     Class Sample:
         pass
3. 指定测试目录 testpath = path
4. 指定忽略某些目录
5. 禁用XPASS

## 2.pytest搜索测试用例的原则：
- 搜索由任何符合以下规则的文件 test_*.py 或 *_test.py 文件。
- 找到后，从这些文件中，收集如下测试项：test 为前缀的函数；Test 为前缀的类里面的以 test 为前缀的函数。

## 3.失败后重跑
1. 安装  pip install pytest-rerunfailures
2. 代码
```python
import pytest
@pytest.mark.smoke
class Sample(object):
    def test_equal(self):
        # 在这里，我让这个case失败，来演示re-run
        assert 1 == 0
    def not_equal(self):
        assert 1 != 0
```
 3. 在命令行运行，失败了的重跑  pytest sample.py --reruns 2
 
 ## 4.pytest并发测试
 1. 安装 pip install pytest-parallel
 2. 在命令行运行,windows环境仅仅支持多线程运行
 ```python
#pytest --workers 2 #指定2个进程并发
#pytest --workers 2 --test-per-worker 3  #指定2个进程并发，每个进程最多运行3个线程
```
 
 ## 5.测试报告
 ### pytest-html
 1. 安装 pip install pytest-html
 2. 在命令行运行 python -m pytest tests/test_ApiTest/test_lagou.py --html=report.html --reruns 2
 ### allure
 1. 安装allure https://blog.csdn.net/chenfei_5201213/article/details/80982929
 2. 在命令行运行 pytest --alluredir=./allure_reports
 3. 在main文件中 运行标记“smoke”的用例 pytest.main(["-m", "smoke", "--alluredir=./allure_reports"])
 4. 修改allure中文乱码
 ```python
# 1.找到如下文件site-packages\pytest_html\plugin.py
# 2.找到如下代码
class TestResult:
  def __init__(self, outcome, report, logfile, config):
      self.test_id = report.nodeid.encode("utf-8").decode("unicode_escape")
# 3.改为如下代码
class TestResult:
  def __init__(self, outcome, report, logfile, config):
      # 白月黑羽修改方法，解决乱码问题
      # self.test_id = report.nodeid.encode("utf-8").decode("unicode_escape")
      self.test_id = report.nodeid
```