class user:

    '''
    The class for the user accounts
    '''

    create_account = []

    def __init__( self, username, email, password, confirmPassword ) :

        '''
        Initializes the class
        '''

        self.username = username
        self.email = email
        self.password = password
        self.confirmPassword = confirmPassword

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
            if user.username == username and user.password == password :
                return user
            return False
