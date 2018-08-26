import string, random
from classes import User, Credentials


def new_account(master_password):

    '''
    Function to create new account
    '''

    new_user = User(master_password) 
    return new_user

def save_account(account):

    '''
    Function to save new account
    '''

    account.save_account()

def validate_user(master_password):

    '''
    Function to validate an existing user
    '''

    existing_user = User.existing_user(master_password)

    return existing_user

def add_credentials(website, email, username, password):

    '''
    Function to create or add credentials for a website
    '''

    credentials = Credential(website, email, username, password)

    return credentials

def save_credentials(credentials):

    '''
    Saves website credentials
    '''

    credentials.save_credentials()

def display_credentials():

    '''
    Returns the saved credentials
    '''

    return Credentials.display_credentials()

def generate_password():

    print('\n')
    print('How many digits would you like your password to have? (From 9 to 15)')

    num = input()

    def generate(passwrd):
            
        '''
        The password generator
        '''

        password = str('')

        for x in range(passwrd):
            x = random.randint(0, 94) 
            password += string.printable[x]
        return password

    if num == '9':
        print('\n')
        print('Your new password is ' + generate(9))
    elif num == '10':
        print('\n')
        print('Your new password is ' + generate(10))
    elif num == '11':
        print('\n')
        print('Your new password is ' + generate(11))
    elif num == '12':
        print('\n')
        print('Your new password is ' + generate(12))
    elif num == '13':
        print('\n')
        print('Your new password is ' + generate(13))
    elif num == '14':
        print('\n')
        print('Your new password is ' + generate(14))
    elif num == '15':
        print('\n')
        print('Your new password is ' + generate(15))
    else:
        print('\n')
        print('Please stick to the given parameters for now. Thanks :)')
        print('\n')

def main():

    '''
    The main menu for the program
    '''
    
    print('\n')
    print('              Pass Manager')
    print('The program that stores all your accounts')
    print('\n')

    while True:
        print("Type 'm' to create a master password; type 'li' to login to existing account.")
        account_logIn = input().lower()

        if account_logIn == 'm':
            print('\n')

            print("Type 'c' to create a password." )
            password_choice = input()

            while True:

                if password_choice == 'c':
                    print('\n')
                    print('Your master password is ')
                    master_password = input()
                    break

                else:
                    print("Please type 'c' to create a password or 'g' to generate one. Thanks :)")
                    print('\n')

            save_account(new_account(master_password))
            print('\n')
            print(f'New Account {master_password} created.')
            break

        elif account_logIn == 'li':

            print('Master password :')
            master_password = input()
            print('\n')

            log_in = validate_user(master_password)
            

            while True:
                print(f"Type 'a' to add a credential; type 's' to see the saved credentials.")
                user_credentials = input() .lower()

                if user_credentials == 'a':
                    
                    print('Type the site you wish to add')
                    site = input()
                    print('\n')
                
                    print('Type in your username for the site')
                    username_input = input()
                    print('\n')

                    print("To create or type in your passcode press 'c'; to generate a passcode press 'g'.")
                    password_input = input()
                    print('\n')

                    while True:
                    
                        if password_input == 'c':
                            print('Your passcode: ')
                            password = input()
                            break

                        elif password_input == 'g':
                            print('\n')
                            password = generate()
                            print('\n')
                            break
                        
                        else:
                            print("Please type 'c' to create a passcode or 'g' to have one generated for you. Thanks :)")
                            break

                            save_credentials(add_credentials(website, email, username, password))
                            print('\n')
                            print(f'{website} : {email} : {username} : {password}')
                            print('\n')

        elif user_credentials == 's':

            print('Enter your passcode:')
            cred_pass = input()
            print('\n')

            if credential_password == master_password:
                display_credentials()
                print('Your Accounts:\n')

                for credential in display_credentials():
                    print(f'Website: {credenitals.website}; Your email: {credential.email} Your username: {credenital.username}; Your password: {credenital.password}')
                    print('\n')

            else:
                print("You currently have no saved credentials. Kindly type 'a' to add one.")
                print('\n')

        elif user_credentials == 'e':
            print('Bye bye...')
            break

        else:
            print('Invalid shortcut! Please try again.')
            print('\n')

if __name__ == '__main__':
    main()
            