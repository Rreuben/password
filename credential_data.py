'''Module containing two classes'''
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
