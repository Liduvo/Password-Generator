from random import choice

print("-----------------------------------------------------------------------------------")
print("                              Python Password Generator                            ")
print(" ")
print("      (1) Generate Random Password    (2)  Creating a Custom Password              ")
print("-----------------------------------------------------------------------------------")

#User entered for password creation selection.
password_type_select = int(input())

uppercase_and_small_letter = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
uppercase_letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
small_letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
special_character = ["+","×","÷","=","/","€","£","¥","₺",")","(","*","&","^","%","$","@","!","-",":",";","?","`","~","|","<",">","{","}","[","]","?","*"]
numbers = [0,1,2,3,4,5,6,7,8,9]
char = []
password_list = []
password = " "

 #User Generate Random Password made selections
if password_type_select == 1:
    print("You Have Chosen To Generate Random Password")
    print("How long is your password?")
    
    #Input for how long the password should be.
    password_length = int(input())

    print("Would you like to use numbers?")
    print("(1) Yes        (2) No  ")
    
    #Entered to use numbers or not in the password.
    password_number_random = int(input())

    print("Do you want special characters in your password?")
    print("(1) Yes        (2) No  ")
    
    #We took input to learn whether special characters (such as $, €) should be used.
    password_special_characters_random = int(input())

    print("Do you want upper/lowercase letters in your password?")
    print("(1) Only Uppercase Letter  (2) Only Small Letter (3) Uppercase Letter and Small Letter")
    #Choose which letters you want used.
    password_letter_random = int(input())


    if  password_number_random == 1 and password_special_characters_random == 1 and password_letter_random == 1:

         char = numbers + special_character + uppercase_letter
         for i in range(password_length):
             password += str(choice(char))


    if password_number_random == 1 and password_special_characters_random == 1 and password_letter_random == 2:

        char = numbers + special_character + small_letter
        for i in range(password_length):
            password += str(choice(char))


    if password_number_random == 1 and password_special_characters_random == 1 and password_letter_random == 3:
        char = numbers + special_character + uppercase_and_small_letter
        for i in range(password_length):
            password += str(choice((char)))


    if password_number_random == 1 and password_special_characters_random == 2 and password_letter_random == 1:
        char = numbers + uppercase_letter
        for i in range(password_length):
            password += str(choice(char))


    if password_number_random == 1 and password_special_characters_random == 2 and password_letter_random == 2:
        char = numbers + small_letter
        for i in range(password_length):
            password += str(choice(char))


    if password_number_random == 1 and password_special_characters_random == 2 and password_letter_random == 3:
        char = numbers + uppercase_and_small_letter
        for i in range(password_length):
            password += str(choice(char))


    if password_number_random == 2 and password_special_characters_random == 1 and password_letter_random == 1:
        char = special_character + uppercase_letter
        for i in range(password_length):
            password += str(choice(char))


    if password_number_random == 2 and password_special_characters_random == 1 and password_letter_random == 2:
        char = special_character + small_letter
        for i in range(password_length):
            password += str(choice(char))


    if password_number_random == 2 and password_special_characters_random == 1 and password_letter_random == 3:
        char = special_character + uppercase_and_small_letter
        for i in range(password_length):
            password += str(choice(char))


    if password_number_random == 2 and password_special_characters_random == 2 and password_letter_random == 1:

         for i in range(password_length):
             password += str(choice(uppercase_letter))


    if password_number_random == 2 and password_special_characters_random == 2 and password_letter_random == 2:

        for i in range(password_length):
            password += str(choice(small_letter))


    if password_number_random == 2 and password_special_characters_random == 2 and password_letter_random == 3:

        for i in range(password_length):
            password += str(choice(uppercase_and_small_letter))

    else:
        print("Try again.")

    print(password)

#User Creating a Custom Password made selections
if password_type_select == 2:
   print("You have chosen the User Login Password.")
   print("How long should the password be?")
   
   #Input for how long the password should be.
   password_length = int(input())

   print("What letters would you like to use in the password?")
   
   #We choose which letters to use.
   password_request = str(input())

   print("Do you want to use numbers and special characters?")
   print("(1) Yes   (2) No")
   
   #Choose which special characters to use.
   password_number_special_characters = int(input())
   if password_number_special_characters == 1:

       print("What numbers and special phrases would you like to have in the password?")

       password_number = int(input())


   for i in password_request:
       password_list += i


   for i in str(password_number):
       password_list += i

   for i in range(password_length):
       password += str(choice(password_list))


   print(password)

