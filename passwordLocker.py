from userData import user
from credentialData import credentialsData
import string, random


def new_users( name_one, name_two, email_address, user_name, pass_word  ) :

    '''
    Creates new user
    '''

    new_user = user( name_one, name_two, email_address, user_name, pass_word ) 

    return new_user

def save_acc( account ) :

    '''
    Saves new account
    '''

    account.save_account()

def check_user( used_name, used_pass ) :

    '''
    Checks for existing user
    '''

    user_exists = user.user_login

    return user_exists

def add_cred( account, account_name, account_pass ) :

    '''
    Adds a credential
    '''

    added_credential = credentialsData( account, account_name, account_pass )

    return added_credential

def save_cred( credential ) :

    '''
    Saves credentials
    '''

    credential.save_credential()

def display_cred() :

    '''
    Returns the saved credential
    '''

    return credentialsData.display()

def delete_cred( credential ) :
    '''
    Deletes a credential
    '''

    credential.delete_credential()

def generate() :

    print( 'How many digits would you like your password to have? (From 9 to 15)' )

    num = input()

    def generatePassword( passwrd ) :
            
        '''
        The password generator
        '''

        password = str( '' )

        for x in range( passwrd ) :
            x = random.randint( 0, 94 ) 
            password += string.printable[ x ]
        return password

    if num == '9' :
        print( '\n' )
        print( 'Your new password is ' + generatePassword( 9 ) )
    elif num == '10' :
        print( '\n' )
        print( 'Your new password is ' + generatePassword( 10 ) )
    elif num == '11' :
        print( '\n' )
        print( 'Your new password is ' + generatePassword( 11 ) )
    elif num == '12' :
        print( '\n' )
        print( 'Your new password is ' + generatePassword( 12 ) )
    elif num == '13' :
        print( '\n' )
        print( 'Your new password is ' + generatePassword( 13 ) )
    elif num == '14' :
        print( '\n' )
        print( 'Your new password is ' + generatePassword( 14 ) )
    elif num == '15' :
        print( '\n' )
        print( 'Your new password is ' + generatePassword( 15) )
    else :
        print( '\n' )
        print( 'Please stick to the given parameters for now. Thanks :)' )
    
def menu() :

    '''
    The main menu for the program
    '''
    print('\n')
    print( 'Welcome to Pass Manager!' )
    print( 'The program that stores all your accounts!' )
    print( '\n' )

    while True :
        print( "Type 'su' to create an account; type 'li' to login to existing account."  )
        account_logIn = input().lower()

        if account_logIn == 'su' :
            print( '\n' )
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
                    print( '\n' )
                    print( 'Your desired password is ' )
                    password = input()
                    break
                elif pass_choice == 'g' :
                    password = generate()
                    break
                else :
                    print( "Please type 'c' to create a password or 'g' to generate one." )
                    break
            save_acc( new_users( firstName, lastName, emails, userName, password) )
            print( '\n' )
            print( f"And your username is { userName }" )
            print( '\n' )
            break

        else account_logIn == 'li' :
            print( 'Please sign up to access this program.\n' )
                
            # print( 'Log in to existing user:\n' )
            # print( 'Username : ' )
            # userName = input()
            # print('\n')

            # print( 'Password : ')
            # password = input()
            # print( '\n' )

            # log_in = check_user( userName, password )
            

        while True :
            print( f"Type 'a' to add a credential; type 's' to see the saved credentials" )
            user_credentials = input() .lower()

            if user_credentials == 'a' :
                print( 'Type the platform you wish to add ' )
                plat_form = input()
                print( '\n' )
                
                print( 'Type in username for the platform' )
                username_input = input()

                print( "To create a passcode type 'c'; to generate a passcode type 'g'" )
                pass_input = input()

                while True :
                    if pass_input == 'c' :
                        print( 'Your passcode: ' )
                        pass2 = input()
                        break
                    elif pass_input == 'g' :
                        print( '\n' )
                        pass2 = generate()
                        print( '\n' )
                        break
                    else :
                        print( "Please type 'c' to create a passcode or 'g' to have one generated for you" )
                        break

                save_cred( add_cred( plat_form, username_input, pass2 ) )
                print( '\n' )
                print( f'{ plat_form } : { user_credentials } : { pass2 }' )
                print( '\n' )
            elif user_credentials == 's' :
                print( 'Enter your passcode: ' )
                cred_pass = input()
                print( '\n' )
                if cred_pass == password :
                    display_cred()
                    print( 'Account details:\n' )
                    for credential in display_cred() :
                        print( f'Platform: { credenital.platform }; Your username: { credenital.username }; Your password: { credenital.password }' )
                        print( '\n' )
                else :
                    print( "You currently have no saved credentials. Kindly type 'a' to add one." )
                    print( '\n' )
            elif user_credentials == 'e' :
                break
            else :
                print( 'Invalid shortcut! Please try again.' )
                print( '\n' )

if __name__ == '__main__' :
    menu()
            