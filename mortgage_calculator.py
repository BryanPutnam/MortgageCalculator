# Author: Bryan Putnam
# Last Updated: 11/10/2021

def intro (): 
    print("This program is designed to take in information about your home purchase and mortgage")
    print("Please follow the steps below")

def is_float (z): 
    try: 
        float(z)
        return True
    except ValueError:
        return False


def house_cost (): 
    print("How much does the house cost in USD?")
    init_cost = input() 
    if is_float(init_cost) is True: 
        new_init_cost = float(init_cost)
    else: 
        print("You must insert a numeric value")
        house_cost()
    down_payment(new_init_cost)


def down_payment (init_cost): 
    print("How much would you like to put down (Percentage)")
    down_cost = input() 
    if is_float(down_cost) is True: 
        new_down_cost = float(down_cost)
    else: 
        print("You must insert a numeric value")
        down_payment(init_cost)
    down = ("%.2f" % (init_cost * (new_down_cost/100)))
    remainder = float("%.2f" % (init_cost - float(down)))
    print(f"Your down payment will be {down}, which leaves {remainder} for the mortgage.")
    mortgage_length(remainder)


def mortgage_length (remainder): 
    print("How many years does the morgage last?")
    mtg_len = input()
    if is_float(mtg_len) is True: 
        new_mtg_len = float(mtg_len)
    else: 
        print("You must use a numeric value")
        mortgage_length()
    rate(new_mtg_len, remainder)


def rate (new_mtg_len, remainder): 
    print("What is your interest rate?")
    interest_rate = input()
    if is_float(interest_rate) is True: 
        new_interest_rate = float(interest_rate)
    else: 
        print("You must use a numeric value")
        rate()
    mortgage_calculator(new_interest_rate, new_mtg_len, remainder)


def mortgage_calculator (new_interest_rate, new_mtg_len, remainder): 
    months = float(new_mtg_len * 12)
    interest_conversion = float(new_interest_rate / 100)
    top = float(remainder * (interest_conversion / 12.00))
    bottom = float(1 - (1 + interest_conversion / 12) ** (-months))
    monthly_pay = float("%.2f" % (top/bottom))
    final = float(monthly_pay * months)
    print(f"You will make {months} payments of {monthly_pay} over {new_mtg_len} years. This will be a total of {final} USD. ")

house_cost()