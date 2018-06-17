class user:

    '''
    The class for the user accounts
    '''

    create_account = []

    def __init__( self, firstName, lastName, username, email, password, ) :

        '''
        Initializes the class
        '''

        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.email = email
        self.password = password
        

    def save_account( self ) :

        '''
        Saves new account details to create_account list
        '''

        user.create_account.append( self )

    @classmethod

    def user_login( cls, used_name, used_pass ) :

        '''
        Authentication process
        '''

        for user in user.create_account :
            if user.username == used_name and user.password == used_pass :
                return user
            return False
