'''Module containing the credentials data'''
class Credentials:

    '''
    Class that will create new instances
    '''

    credentials = []

    def __init__(self, website, email, username, password):

        self.website = website
        self.email = email
        self.username = username
        self.password = password

    def save_credentials(self):

        '''
        Saves credential objects to credentials
        '''

        Credentials.credentials.append(self)

    @classmethod
    def display_credentials(cls):

        '''
        Returns the credentials
        '''

        return cls.credentials

class User:

    '''
    Class that will create accounts for users
    '''

    user_accounts = []

    def __init__(self, master_password):

        '''
        Initializes the class
        '''

        self.master_password = master_password

    def save_account(self):

        '''
        Saves new master password to user_accounts list
        '''

        User.user_accounts.append(self)

    @classmethod
    def existing_user(cls, master_password):

        '''
        Authentication process
        '''

        for user in User.user_accounts:
            if user.master_password == master_password:
                return user
            return False
