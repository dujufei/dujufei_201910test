#-*- encoding: utf-8 -*-
# .使用Unittest单元测试框架实现数据和接口的自动化测试
# 单个测试用例
import unittest
class Mytestcase(unittest.TestCase):
    def setUp(self):
        a = {'a':'a','b':'b'}
        b = {'b':'b','a':'a'}
        self.assertEqual(a, b, 'eror')
        print('pre-test')

    def testcase(self):
        print('in-test')

    def tearDown(self):
        print('test-over')

if __name__ == '__main__':
    unittest.main()


