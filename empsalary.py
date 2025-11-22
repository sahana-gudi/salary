import sys

def calculate_bonus(salary):
    bonus = salary * 0.10
    total_salary = salary + bonus
    return bonus, total_salary

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python salary_bonus.py <salary>")
        sys.exit(1)

    try:
        salary = float(sys.argv[1])
        bonus, total_salary = calculate_bonus(salary)
        print(f"Bonus Amount: {bonus:.2f}")
        print(f"Total Salary after adding bonus: {total_salary:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric salary value.")
