import unittest
from validation import Validator

class ValidationTests(unittest.TestCase):
    inputs={}
    rules={}
    vdt=None

    def init(self):
        self.vdt = Validator.make(self.inputs, self.rules)

    def tearDown(self):
        self._inputs={}
        self._rules = {}
        self.vdt = None

    def test_emptyrules(self):
        self.init()
        self.assertEqual(self.vdt.fails(), False) #valiadtion (passes)

    def test_emptydata(self):
        self.rules={'name':'req|num'}
        self.init()
        self.assertEqual(self.vdt.fails(), True) #valiadtion depends on rules (fails)

    def test_bail(self):
        self.inputs={'age':'18', 'name':'evance soumaoro'}
        self.rules={'age': 'num|bail|min:14', 'name':'req'}
        self.init()
        self.assertEqual(self.vdt.fails(), False) #valiadtion (pass)

    def test_req(self):
        self.inputs={'age':'18', 'fname':'', 'lname':'   '}
        self.rules={'age': 'num', 'fname':'req', 'lname':'req'}
        self.init()
        self.assertEqual(self.vdt.fails(), True) #valiadtion (fails)

    def test_num(self):
        self.inputs={'age':'18', 'exp':3.5}
        self.rules={'age': 'num','exp':'num'}
        self.init()
        self.assertEqual(self.vdt.fails(), False) #valiadtion (passes)

    def test_int(self):
        self.inputs={'age':'18', 'exp':3}
        self.rules={'age': 'int','exp':'int'}
        self.init()
        self.assertEqual(self.vdt.fails(), False) #valiadtion (passes)

    def test_min(self):
        self.inputs={'name':'evance', 'age':'18.5', 'exp':3 , 'height':1.65}
        self.rules={'name':'min:3','age': 'num|min:12','exp':'int|min:2', 'height':'num|min:1'}
        self.init()
        self.assertEqual(self.vdt.fails(), False) #valiadtion (passes)

    def test_max(self):
        self.inputs={'name':'evance', 'age':'18', 'exp':3 , 'height':5.65}
        self.rules={'name':'max:7','age': 'num|max:30','exp':'int|max:3', 'height':'num|max:7'}
        self.init()
        self.assertEqual(self.vdt.fails(), False) #valiadtion (passes)

    def test_between(self):
        self.inputs={'name':'evance', 'age':'18', 'exp':3 , 'height':5.65}
        self.rules={'name':'req|btw:3,7','age': 'num|btw:10,30','exp':'int|btw:3,5'}
        self.init()
        self.assertEqual(self.vdt.fails(), False) #valiadtion (passes)







if __name__ == '__main__':
    unittest.main()
