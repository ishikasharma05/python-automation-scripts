try:
    with open("server.log", "r") as file:
        logs = file.read()

except FileNotFoundError:
    print("Log file not found.")

else:
    print(logs)

finally:
    print("Log check completed.")


<img width="508" height="53" alt="image" src="https://github.com/user-attachments/assets/8839c640-5d86-4abb-b561-2582911f0019" />
