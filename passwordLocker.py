from userData import user
from credentialData import credentialsData
from passGen import passwordGen


def new( name_one, name_two, email_address, pass_word  ) :

    '''
    Creates new user
    '''

    new_user = userData( name_one, name_two, email_address, pass_word ) :

    return new_user

def save( account ) :

    '''
    Saves new account
    '''

    account.save_account()

def check( used_name, used_pass ) :

    '''
    Checks for existing user
    '''

    user_exists = user.user_login( used_name, used_pass )

    return user_exists

def add( account, account_name, account_pass ) :

    '''
    Adds a credential
    '''

    added_credential = credentialsData( account, account_name, account_pass )

    return added_credential

def save( credential ) :

    '''
    Saves credentials
    '''

    credential.save_credential()






def menu() :

    '''
    The main menu for the program
    '''
    print('\n')
    print( 'Welcome to Pass Manager!' )
    print( 'The program that stores all your accounts' )

    while True :
        print( "Type 'su' to create an account; type 'li' to login to existing account."  )
        account_logIn = input() .lower()

        if account_logIn == 'SU' :
            print( 'What\'s your first name?' )
            firstName = input()
            print( '\n' )

            print( 'And your last name?' )
            lastName = input()
            print( '\n' ) 
                
            print( 'Your username :' )
            userName = input()
            print( '\n' )

            print( 'And your email :' )
            emails = input()
            print('\n')

            print( "To create a password, type 'c'; to generate a password, type 'g'" )
            pass_choice = input()

            while True :
                if pass_choice == 'c' :
                    print( 'Your desired password :' )
                    password = input()
                    break
                elif pass_choice == 'g' :
                    print( generate() )
                    break
                else :
                    print( "Please type 'c' to create a password or 'g' to generate one." )
                    break
                
