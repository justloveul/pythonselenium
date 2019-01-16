import unittest, os
from public import openFile
from public.HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner

basepath = os.path.dirname(__file__)
testpath = os.path.join(basepath, 'testCase')
f = openFile.open_report_file(basepath)
discover = unittest.defaultTestLoader.discover(testpath)
runner = HTMLTestRunner(stream=f, title="自动化测试报告")
runner.run(discover)
f.close()
