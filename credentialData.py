class credentialData :

    '''
    Creates new instances for the credential inputs
    '''

    credentials = []

    def __init__( self, platform, username, password ) :

        self.platform = platform
        self.username = username
        self.password = password

    def save( self ) :

        '''
        Saves the account details
        '''

        credentialData.credentials.append( self )

    @classmethod

    def display( cls ) :

        '''
        Displays the account details
        '''

        return cls.credentials

    @classmethod

    def delete( cls ) :

        '''
        Deletes the account details
        '''

        credentialData.credentials.remove( cls )