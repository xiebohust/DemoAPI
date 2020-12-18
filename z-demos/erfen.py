import os,sys
import unittest,requests


sys.path.append(os.path.dirname(__file__))
print(sys.path)





path = os.path.dirname(__file__)
cases = unittest.defaultTestLoader.discover(path,pattern='*api.py')

filename = 'ceshi.txt'
fp = open(filename,'a')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='baogao')
runner = unittest.TextTestRunner(stream=fp,verbosity=2)
runner.run(cases)
# HTMLTestRunner.main()





#
# class TT(unittest.TestCase):
#
#     def setUp(self):
#         self.k = {'a':1,'b':2}
#
#
#
#     def tests(self):
#         self.assertIn('a',self.k)
#         self.assertIn('b',self.k)





