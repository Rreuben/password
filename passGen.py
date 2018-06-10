import string, random

class passwordGen :

    def generate( self ) :

        print( 'How many digits would you like your password to have? (From 9 to 15)' )

        num = input()

        def generatePassword( passwrd ) :
            
            '''
            The password generator
            '''

            password = str('')

            for x in range( passwrd ) :
                x = random.randint( 0, 94 ) 
                password += string.printable[ x ]
            return password

        if num == '9' :
            print( 'Your new password is : ' + generatePassword( 9 ) )
        elif num == '10' :
            print( 'Your new password is : ' + generatePassword( 10 ) )
        elif num == '11' :
            print( 'Your new password is : ' + generatePassword( 11 ) )
        elif num == '12' :
            print( 'Your new password is : ' + generatePassword( 12 ) )
        elif num == '13' :
            print( 'Your new password is : ' + generatePassword( 13 ) )
        elif num == '14' :
            print( 'Your new password is : ' + generatePassword( 14 ) )
        elif num == '15' :
            print( 'Your new password is : ' + generatePassword( 15) )
        else :
            print( 'Please stick to the given parameters for now. Thanks :)' )
