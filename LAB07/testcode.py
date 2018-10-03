import Code
import unittest
class TestCode (unittest.TestCase):
        def test_correct_user_password(self):
                self.assertEqual(Code.login('thirawat','1212312121'),1)
        def test_correct_user_wrong_password(self):
                self.assertEqual(Code.login('thirawat','abc123'),0)
        def test_wrong_user_correct_password(self):
                self.assertEqual(Code.login('thirawas1','1212312121'),0)
        def test_wrong_user_wrong_password(self):
                self.assertEqual(Code.login('thirawat456','123123abc'),0)
if __name__ == '__main__':
        unittest.main()
