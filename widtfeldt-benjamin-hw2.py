def sales_tax():
    nonfloatinput = input("Enter the amount of the purchase: ")
    state_rate = .05
    county_rate = .025
    user_input = format(float(nonfloatinput),'.2f')
    state_tax = format(float(user_input) * float(state_rate) , '.2f')
    county_tax = format(float(user_input) *float(county_rate), '.2f')
    total_tax = format(float(state_tax) + float(county_tax) ,'.2f')
    total_sale = format(float(user_input) + float(total_tax) , '.2f')

    print("Purchase Amount: " + str(user_input))
    print("State Tax: " + str(state_tax))
    print("County Tax: " + str(county_tax))
    print("Total Tax: " + str(total_tax))
    print("Sale Total: " + str(total_sale))

def compound_interest():
    user_principal = float(input("Enter the starting principal: "))
    user_interest = float(input("Enter the annual interest rate: ")) / 100
    user_compounding = float(input("How many times per year is the interest compounded? "))
    user_period = float(input("For how many years will the account earn interest? "))

    unrounded_future_value = user_principal * (1 + (user_interest / user_compounding)) ** (user_compounding * user_period)
    future_value = format(float(unrounded_future_value),'.2f')
    user_period = format(user_period, '.0f')

    print("At the end of " + str(user_period) + " years you will have $ " + str(future_value))


def dollar_game():
    user_pennies = float(input("Enter the number of pennies: "))
    user_nickels = float(input("Enter the number of nickels: "))
    user_dimes = float(input("Enter the number of dimes: "))
    user_quarters = float(input("Enter the number of quarters: "))

    total_value = user_pennies + (user_nickels*5) + (user_dimes*10) + (user_quarters*25)

    if total_value < 100:
        print("Sorry, the amount you entered was less than one dollar.")
    elif total_value > 100:
        print("Sorry, the amount you entered was more than one dollar.")
    elif total_value == 100:
        print("Congratulations!")
        print("The amount you entered was exactly one dollar!")
        print("You win the game!")

def quantity_discount():
    user_packages = int(input("Enter the number of packages purchased: "))
    total_price = user_packages * 99
    discount = float(0)

    if user_packages >=0 and user_packages <10:
        discount = 0
    elif user_packages >= 10 and  user_packages <= 19:
        discount = .1
    elif user_packages >= 20 and user_packages <= 49:
        discount = .2
    elif user_packages >= 50 and user_packages <= 99:
        discount =.3
    elif user_packages >= 100:
        discount =.4

    subtotal = format(total_price - discount*total_price, '.2f')
    discount_total = format(discount*total_price, '.2f')
    print("Discount Amount: $ " + str(discount_total))
    print("Total Amount: $ " + str(subtotal))

def shipping_charge():
    user_weight = float(input("Enter the weight of the package: "))
    rate_per_pound = 0

    if user_weight >= 0 and user_weight <= 2:
        rate_per_pound = 1.5
    elif user_weight > 2 and user_weight <= 6:
        rate_per_pound = 3
    elif user_weight > 6 and user_weight <= 10:
        rate_per_pound = 4
    elif user_weight > 10:
        rate_per_pound = 4.75

    shipping_total = format(rate_per_pound * user_weight, '.2f')
    print("Shipping charge: $ " + str(shipping_total))

def budget_analysis():

    budget = float(input("Enter amount budgeted for the month: "))
    spent = float(input("Enter an amount spent(0 to quit): "))

    while spent != 0:
        expense = float(input("Enter an amount spent(0 to quit): "))
        spent = spent + expense
        if expense == 0:
            break

    budget = format(float(budget), '.2f')
    spent = format(float(spent), '.2f')
    under = format(float(budget) - float(spent), '.2f')
    over = format(float(spent) - float(budget), '.2f')
    
    print("Budgeted: $ " + str(budget))
    print("Spent: $ " + str(spent))

    budget = float(budget)
    spent = float(spent)

    if budget < spent:
        print("You are $ " + str(over) + " over budget. PLAN BETTER NEXT TIME")
    if budget == spent:
        print("Spending matches budget. GOOD PLANNING!")
    if budget > spent:
        print("You are $ " + str(under) + " under budget. WELL DONE!" )

def average_rainfall():
    #how I initially wrote the code:

    # years = float(input("Enter the number of years: "))
    # starting_year = 1
    # total_rainfall = float(0)
    # while starting_year <= years:
    #     print("For year " + str(starting_year) + ":")
    #     month_1 = float(input("Enter the rainfall amount for the month: "))
    #     month_2 = float(input("Enter the rainfall amount for the month: "))
    #     month_3 = float(input("Enter the rainfall amount for the month: "))
    #     month_4 = float(input("Enter the rainfall amount for the month: "))
    #     month_5 = float(input("Enter the rainfall amount for the month: "))
    #     month_6 = float(input("Enter the rainfall amount for the month: "))
    #     month_7 = float(input("Enter the rainfall amount for the month: "))
    #     month_8 = float(input("Enter the rainfall amount for the month: "))
    #     month_9 = float(input("Enter the rainfall amount for the month: "))
    #     month_10 = float(input("Enter the rainfall amount for the month: "))
    #     month_11 = float(input("Enter the rainfall amount for the month: "))
    #     month_12 = float(input("Enter the rainfall amount for the month: "))
    #     total_rainfall = total_rainfall + month_1 + month_2 + month_3 + month_4 + month_5 + month_6 + month_7 + month_8 + month_9 + month_10 + month_11 + month_12
    #     starting_year += 1
    
    # total_months = years * 12
    # average_rain = total_rainfall / total_months
    
    # total_rainfall = format(float(total_rainfall),'.2f')
    # total_months = format(float(total_months),'.2f')
    # average_rain = format(float(average_rain),'.2f')

    # print("For " + str(total_months) + " months")
    # print("Total rainfall:  " + str(total_rainfall) + " inches")
    # print("Average monthly rainfall:  " + str(average_rain) + " inches")

    #how I wrote it with nested loops (both work)

    years = int(input("Enter the number of years: "))
    starting_year = int(1)
    total_rainfall = float(0)

    for i in range(starting_year, (years +1)):
        print("For year  " + str(starting_year) + " :")

        for j in range(1,13):
            month_rainfall = float(input("Enter the rainfall amount for the month: "))
            total_rainfall = total_rainfall + month_rainfall
        starting_year += 1

    total_months = years * 12
    average_rain = total_rainfall / total_months

    total_rainfall = format(float(total_rainfall),'.2f')
    total_months = int(total_months)
    average_rain = format(float(average_rain),'.2f')

    print("For  " + str(total_months) + " months")
    print("Total rainfall:  " + str(total_rainfall) + " inches")
    print("Average monthly rainfall:  " + str(average_rain) + " inches")


def factorial():
    number = int(input("Enter a nonnegative integer: "))
    start = 0
    factorial = 1

    if number < 0:
        print("Error: Number is negative")
    else:
        for start in range(0,number):
            factorial = (start + 1) * factorial
            start += 1
        print("The factoral of " + str(number) + " is " + str(factorial))

def morse_code():
    user_string = input("Enter the string to be converted to Morse code: ")

    master_list = {'A': '.-',     'B': '-...',   'C': '-.-.', 
                   'D': '-..',    'E': '.',      'F': '..-.',
                   'G': '--.',    'H': '....',   'I': '..',
                   'J': '.---',   'K': '-.-',    'L': '.-..',
                   'M': '--',     'N': '-.',     'O': '---',
                   'P': '.--.',   'Q': '--.-',   'R': '.-.',
                   'S': '...',    'T': '-',      'U': '..-',
                   'V': '...-',   'W': '.--',    'X': '-..-',
                   'Y': '-.--',   'Z': '--..',

                   'a': '.-',     'b': '-...',   'c': '-.-.', 
                   'd': '-..',    'e': '.',      'f': '..-.',
                   'g': '--.',    'h': '....',   'i': '..',
                   'j': '.---',   'k': '-.-',    'l': '.-..',
                   'm': '--',     'n': '-.',     'o': '---',
                   'p': '.--.',   'q': '--.-',   'r': '.-.',
                   's': '...',    't': '-',      'u': '..-',
                   'v': '...-',   'w': '.--',    'x': '-..-',
                   'y': '-.--',   'z': '--..',


                   '0': '-----',  '1': '.----',  '2': '..---',
                   '3': '...--',  '4': '....-',  '5': '.....',
                   '6': '-....',  '7': '--...',  '8': '---..',
                   '9': '----.', 

                   ' ': ' ',      ',': '--..--', '.': '.-.-.-',
                   '?': '..--..',
                   }
           
    for x in user_string:
        if x != " ":
            print(master_list[x] + ",", end="")
        else:
            print(" ", end="")


    print("\n", end="")



def main():
    sales_tax()
    compound_interest()
    dollar_game()
    quantity_discount()
    shipping_charge()
    budget_analysis()
    average_rainfall()
    factorial()
    morse_code()

if __name__=="__main__":
    main()