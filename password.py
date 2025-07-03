import secrets
import string
import re  # regex {regular expression}


def menu():
    
   while True: 
    print("Welcome")
    print("1. Choose your own password")
    print("2. use our suggested strong password")
    print("3. Exit")
    
    choice = input("Enter your choice : ")
    if choice == '1':
        
        password = input("Enter your password : ")
        password_validator(password)
        
    elif choice == '2':
        password = generate_strong_password()
        print(f"Your password is {password}")
        
    elif choice == '3':
        print("You are exiting the program")
        break
        
    else:
        
        print("wrong choice")


    
    


# a function which generate strong password for user
def generate_strong_password(length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

  
    password = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_chars = lower + upper + digits + symbols
    password += [secrets.choice(all_chars) for _ in range(length - 4)]

   
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)




def password_validator(password):
        
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    length = len(password)
    
    
    if has_lower and has_upper and has_digit and has_special and length >=8 :
        print("Your password is strong")
        
    
    else:
        
   
            if not has_lower:
                print("Password must contain at least one lower character")
            
            if not has_upper:
                print("Password must contain atleast one upper character")
                
            if not has_digit:
                print("Password must contain atleast one digit")
                
            if not has_special:
                print("Password must contain atleast one special character")
                
            if length < 8:
                print("Password must be at least 8 characters long.")
                
            
         
          
    
menu()  # main entry program
    
    
    
# we can also validate password using regex


def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%!^&*])[A-Za-z\d@#$%!^&*]{8,}$'
    
    if re.fullmatch(pattern, password):
        print("Password is strong")
    else:
        print("Your password is not strong")

# validate_password("1234567Assss3#")