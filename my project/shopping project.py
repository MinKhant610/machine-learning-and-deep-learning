"""
1 Cocacola
2 Suprise
3 Yoshi
4 Fire Dragon
5 Shark
"""
print (__doc__)

def caculator():
    
    user_amount =int(input ('Enter pay money :'))
    
    output = True
    
    if user_input==1 :
        result = user_amount - 500
    elif user_input == 2 :
        result = user_amount - 500
    elif user_input==3 :
        result = user_amount - 300
    elif user_input==4 :
        result = user_amount - 350
    elif user_input==5 :
        result = user_amount - 700
    else :
        output = False
        print ('Wrong')
    if output :
        print ('Refund ',result)

user_input = int(input ('Choose the number that you Want To Drink : '))

if user_input == 1 :
    print ('The price is 500 kyats')
    caculator()

elif user_input == 2 :
    print ('The price is 500 kyats')
    caculator()

elif user_input == 3 :
    print ('The price is 300 kyats')
    caculator()

elif user_input == 4 :
    print ('The price is 350 kyats')
    caculator()

elif user_input == 5 :
    print ('The price is 700 kyats')
    caculator ()

else :
    print ('Plese enter number only and you can choose 1 to 5')

exit = input (' Press Enter to exit')



