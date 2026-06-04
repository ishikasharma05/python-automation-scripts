class LowBalanceError(Exception):
    pass

try:
    balance = int(input("Enter Balance: "))

    if balance < 1000:
        raise LowBalanceError

    print("Withdrawal Allowed")

except LowBalanceError:
    print("Minimum balance should be ₹1000")

finally:
    print("Transaction Complete")


<img width="514" height="121" alt="image" src="https://github.com/user-attachments/assets/207e246f-7ff1-4427-92f7-33a5240b72f2" />
