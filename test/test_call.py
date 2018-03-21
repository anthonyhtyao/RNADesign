import unittest
from utils.call import get_float

class CallFunctionTest(unittest.TestCase):
    """
    Test Vienna Package caller
    """
    def test_get_float(self):
        """
        Test auxiliar function, get_float
        """
        text = "tedx10.23s\nenergy -32.25\t   lfs+sd"
        true = [10.23,-32.25]
        self.assertEqual(true, get_float(text))

if __name__ == "__main__":
    unittest.main()
