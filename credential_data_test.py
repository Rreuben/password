'''Unit test module for Credentials class'''
import unittest
from credential_data import Credentials

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Youtube", "user@mail.com", "user123", "12345qwerty")

    def test_init(self):
        '''
        Test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_credential.website, "Youtube")
        self.assertEqual(self.new_credential.email, "user@mail.com")
        self.assertEqual(self.new_credential.username, "user123")
        self.assertEqual(self.new_credential.password, "12345qwerty")

    def tearDown(self):
        '''
        Clear after each test case runs
        '''
        Credentials.credentials = []

    def test_save_credentials(self):
        '''
        Test case to test if the contact object is saved into the credentials list.
        '''
        self.new_credential.save_credentials()
        youtube = Credentials("Youtube", "user@mail.com", "user123", "12345qwerty")
        youtube.save_credentials()
        self.assertEqual(len(Credentials.credentials), 2)

    def test_display_credentials(self):
        '''
        Test case to test if the contact object is returned.
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials)

if __name__ == '__main__':
    unittest.main()
