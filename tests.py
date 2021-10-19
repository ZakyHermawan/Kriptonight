import unittest
from stream import * 

class StreamTest(unittest.TestCase):
    def testShift(self):
        self.assertEqual(shift("Abcd2", 3), "Defg2")
    
    def testUnshift(self):
        self.assertEqual(unshift("Defg2", 3), "Abcd2")

if __name__ == '__main__':
    unittest.main()
