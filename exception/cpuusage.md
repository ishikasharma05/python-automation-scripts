try:
    cpu_usage = int(input("Enter CPU Usage: "))

    if cpu_usage > 90:
        print("High CPU Usage Alert!")

except ValueError:
    print("CPU usage must be a number.")

finally:
    print("Monitoring completed.")

    <img width="495" height="56" alt="image" src="https://github.com/user-attachments/assets/4f154326-0787-4f5e-88fa-d69f62ab8f44" />
