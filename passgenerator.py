import random 
import string

'''
This project is about creating a password generator that will generate random strings that includes
'''

def passgenerator(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters   
    digits = string.digits           
    special = string.punctuation     
   
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    
    pwd = ""
    meets_criteria = False  
    has_number = False
    has_special = False
    
    '''
    While we do not meet the criteria or if the length of the password is not yet equal to or 
    greater than the minimum length. It will continue to keep adding characters to the password 
    until it meets the requirements
    '''
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters) 
        pwd += new_char 

    
        if new_char in digits:
            has_number = True
        
        elif new_char in special:
            has_special = True

       
        meets_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)?").lower() == "y"
has_special = input("Do you want to have special characters (y/n)?").lower() == "y"


pwd = passgenerator(min_length, has_number, has_special)
print("The recommended password for you is:", pwd) 
