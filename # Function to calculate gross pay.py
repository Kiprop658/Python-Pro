
def calculate_gross_pay(hours_worked, rate_per_hour):
    return hours_worked * rate_per_hour

def main():
        hours_worked = float(input("Enter the number of hours worked: "))
        rate_per_hour = float(input("Enter the rate per hour: "))
        gross_pay = calculate_gross_pay(hours_worked, rate_per_hour)
        print(f"The gross pay is: ${gross_pay:.2f}")
if __name__ == "__main__":
    main()