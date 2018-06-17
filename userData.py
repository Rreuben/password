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

    def user_login( cls, username, password ) :

        '''
        Authentication process
        '''

        for user in user.create_account :
            if user.username == user_name and user.password == used_password :
                return user
            return False
