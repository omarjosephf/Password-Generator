import random 
import string

'''
This project is about creating a password generator that will generate random strings that includes

'''
# This function will generate the password
# It has parameters that has minimum length which will be the length of the password
'''
numbers and special_character are set to True so we can specify if we want the password
to generate numbers or special characters.
'''
def passgenerator(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters   #This generates strings from the alphabet with lower and uppercase letters
    digits = string.digits           #This generates strings that include numbers from 0 to 9
    special = string.punctuation     #This generates strings that are punctuation marks

    #This gives a new name for letters as characters. 
    #This follows up on what happens if the numbers or special_characters are True.
    #Characters(letters) will combine with numbers and punctuation if numbers or special_characters is True.
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    #This is where the password will be stored
    pwd = ""
    #This will only become True once the password meets the criteria that includes at least 1 digit and special.
    #Otherwise False.
    meets_criteria = False  
    #This variable informs us if we do have a number in our password.
    has_number = False
    #This variable informs us if we do have a special_character(punctuations) in our password.
    has_special = False
    
    '''
    While we do not meet the criteria or if the length of the password is not yet equal to or 
    greater than the minimum length. It will continue to keep adding characters to the password 
    until it meets the requirements
    '''
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters) #This generates random characters 
        pwd += new_char #The new characters will be stored and combined with the password.

        
        if new_char in digits:
            has_number = True
        
        elif new_char in special:
            has_special = True

        #meets_criteria will only become True when the criteria is met.
        meets_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)?").lower() == "y"
has_special = input("Do you want to have special characters (y/n)?").lower() == "y"

#This will execute the program
pwd = passgenerator(min_length, has_number, has_special)
print("The recommended password for you is:", pwd) #This will print the password generated for the user.