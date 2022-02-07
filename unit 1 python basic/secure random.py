#Secure random
#This is secret random
#This secret random is used for reset code or token

import secrets
print('Printing secret module')

secure_generator = secrets.SystemRandom()
random_number = secure_generator.randint(0,10)
print('Secret random number is ',random_number)

secure_generator2 = secrets.SystemRandom()
random_number2 = secure_generator2.randrange(2,10,2)
print('Secret randrange number2 is ',random_number2)

number_list = [1,2,3,4,5,6,7]
secure_generator3 = secrets.SystemRandom()
random_choice = secure_generator3.choice(number_list)
print ('Secure choice ',random_choice)


print (secrets.token_bytes(2))
print (secrets.token_hex(2)) #1 bit change two hex digits

#to use secrets.token_usrlsafe

password_reset_link = "http://www.minkhant.com/reset="
password_reset_link += secrets.token_urlsafe(32)
print ('Generating secret URL link',password_reset_link)

