__author__ = 'liangdong'

# define main and call the two functions
def main():
    input_number = get_user_input()
    calculate_correct_amount_of_change(input_number)

# get user's input as the price for the item and return it
def get_user_input():
    user_input = int(input("Enter price of item (from 25 cents to $1, in 5-cent increments): "))
    # deal with the "1 dollar" situation
    if (user_input == 1):
        user_input = 100
    # control user's input
    if (user_input < 25 or user_input > 100):
        print "\nPlease re-enter a price between 25 cents and 1 dollar. ^^"
        exit()
    else:
        return user_input

# use an argument to calculate the numbers of quarters, dimes and nickels needed to make the correct change
def calculate_correct_amount_of_change(cost_of_item):
    print "\nYou bought an item for", cost_of_item, "cents and gave me a dollar."
    # calculate the total change
    Total_change = int(100 - cost_of_item)
    # calculate the number of quarters/dimes/nickels needed
    number_of_quarters = Total_change / 25
    number_of_dimes = (Total_change - 25 * number_of_quarters) / 10
    number_of_nickels = (Total_change - 25 * number_of_quarters - 10*number_of_dimes) / 5
    # use if-else statements to decide whether to use singular or plural form in the output
    if (number_of_quarters == 1):
        output_quarters = "quarter"
    else:
        output_quarters = "quarters"
    if (number_of_dimes == 1):
        output_dimes = "dime"
    else:
        output_dimes = "dimes"
    if (number_of_nickels == 1):
        output_nickels = "nickel"
    else:
        output_nickels = "nickels"
    # output the result
    print "\nYour change is", number_of_quarters, output_quarters + ",", number_of_dimes, output_dimes + ", and", number_of_nickels, output_nickels + "."

# call main()
main()




