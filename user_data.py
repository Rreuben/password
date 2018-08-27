'''Module containing the user data'''
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