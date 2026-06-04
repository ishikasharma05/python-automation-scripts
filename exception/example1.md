try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Please enter only numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result =", result)

finally:
    print("Program Finished")

<img width="499" height="152" alt="image" src="https://github.com/user-attachments/assets/08e2c313-6e02-4a46-b128-4e737cf68a23" />
