# Write your code here


def current_savings1():
    total_cost = int(input("What is the price of your dream home ? "))
    annual_salary = int(input("What is your annual salary? "))
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    portion_saved = 0.1
    months = 0
    monthly_salary = (annual_salary / 12)
    monthly_saved = monthly_salary * portion_saved
    while current_savings < portion_down_payment * total_cost:
        print(current_savings)
        months += 1
        interest_earned = ((current_savings * r) / 12)
        current_savings += monthly_saved + interest_earned
    print(current_savings)
    print(months)


current_savings1()


def current_savings2():
    total_cost = int(input("What is the price of your dream home version 2? "))
    annual_salary = int(input("What is your annual salary version 2? "))
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    portion_saved = 0.15
    months = 0
    monthly_salary = (annual_salary / 12)
    monthly_saved = monthly_salary * portion_saved
    while current_savings < portion_down_payment * total_cost:
        print(current_savings)
        months += 1
        interest_earned = ((current_savings * r) / 12)
        current_savings += monthly_saved + interest_earned
    print(current_savings)
    print(months)


current_savings2()

def current_savings3():
    total_cost = int(input("What is the price of your dream home version 3? "))
    annual_salary = int(input("What is your annual salary version 3? "))
    portion_down_payment = float(input("What percent do you need of the total cost? enter as decimal: "))
    current_savings = 0
    r = float(input("What is your annual rate of return? enter as decimal: "))
    portion_saved = float(input("what percent do you want to save per month? enter as decimal: "))
    months = 0
    monthly_salary = (annual_salary / 12)
    monthly_saved = monthly_salary * portion_saved
    while current_savings < portion_down_payment * total_cost:
        print(current_savings)
        months += 1
        interest_earned = ((current_savings * r) / 12)
        current_savings += monthly_saved + interest_earned
    print(current_savings)
    print(months)


current_savings3()