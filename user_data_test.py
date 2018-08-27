'''Unit test module for User class'''
import unittest
from user_data import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = User("qwerty12345")

    def test_init(self):
        '''
        Test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_account.master_password, "qwerty12345")

    def tearDown(self):
        '''
        Clear after each test case runs
        '''
        User.user_accounts = []

    def test_save_account(self):
        '''
        Test case to test if the account object is saved into the user_accounts list.
        '''
        self.new_account.save_account()
        self.assertEqual(len(User.user_accounts), 1)

if __name__ == '__main__':
    unittest.main()
