# coding=utf-8
import unittest
import test_Baidu
import test_Youdao
import time
from HTMLTestRunner import HTMLTestRunner

#Construct testSuites

suite = unittest.TestSuite()
suite.addTest(test_Baidu.MyTest("test_baidu"))
suite.addTest(test_Youdao.MyTest("test_youdao"))

if __name__ == "__main__":
    now = time.strftime("%d-%m-%y %H_%M_%S")
    filename = './' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='webTest', description='testCase :')

    #runner = unittest.TextTestRunner()
    runner.run(suite)
    fp.close()