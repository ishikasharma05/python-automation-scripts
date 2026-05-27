# ATM PIN Validator
# Simulates an ATM pin entry system
# Allows maximum 3 attempts before blocking the card

correct_code = 231001
attempts = 0

while attempts < 3:
    user_code = int(input("Enter your 6 digit code: "))
    
    if user_code == correct_code:
        print("Access granted. You have entered the correct PIN.")
        break
    else:
        attempts += 1
        remaining = 3 - attempts
        if attempts == 3:
            print("Your card has been blocked due to too many incorrect attempts.")
        else:
            print(f"Incorrect PIN. You have {remaining} attempt(s) remaining.")
