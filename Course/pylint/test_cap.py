import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        test = 'python'
        result = cap.cap_text(test)
        self.assertEqual(result,'python')

if __name__ == '__main__':
    unittest.main()