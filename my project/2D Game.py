import secrets

secure_number = secrets.SystemRandom()

while True:
    print ('____welcome to our game ____')
    press1 = int (input('Press 1 to Read Rule or Press to 2 To Play game :>'))

    if press1 == 1 :
        print('>Age must be more than 18')
        print('>Show money more than 5000')
        print ('> U must use more than 1000 each time')
    
    if press1 == 2:
        user_name = input ('Please enter your name:')
        user_age = int(input ('Please enter your age :>'))

        while len(user_name) > 2 and user_age > 17 :
            print ('You can play game now ')
            print ('Welcome :>',user_name)
            
            while True:
                show_money = int(input('Please enter your show money :'))
                while show_money > 4999:
                    while True:
                        print('This is your money $',show_money)
                        input_money = int (input('Please enter money to play :'))
                        lucky_number= int (input('Please enter your lucky number :'))
                        system_number = secure_number.randint(10,99)
                        while lucky_number == system_number:
                            print ("You win $",input_money)
                        print ("Sorry you lose $",input_money,"The lucky_number is",system_number)
                        show_money=show_money - input_money

                        if show_money < 1000:
                            print ('You have not enought money')
                            break
                        
                print ("Please more money")

        print ('Please read again the rule')

