__author__ = 'liangdong'

def main():
    # define output sentences
    result_comp_wins = "The computer has won this round."
    result_user_wins = "You win!"
    result_tied = "It's a tie!"
    # define the number of times the user selected each weapon
    count_rock = count_paper = count_scissors = 0
    # define the number of times computer won / user won / tied
    count_comp_wins = count_user_wins = count_tied = 0
    print "Let's play Rock, Paper, Scissors!"
    user_input = get_user_input()
    # if the user entered nothing, prompt the user again
    if user_input.__eq__(""):
        print "Please enter a valid input!\n"
        user_input = get_user_input()
    # while loop to avoid Q or q
    while user_input.__ne__('Q') and user_input.__ne__('q'):
        comp_weapon = choose_weapon()
        # get the weapon the user chose and count the number of times the user selected each weapon
        if user_input.__eq__('R') or user_input.__eq__('r'):
            user_weapon = "rock"
            count_rock +=1
        elif user_input.__eq__('P') or user_input.__eq__('p'):
            user_weapon = "paper"
            count_paper +=1
        else:
            user_weapon = "scissors"
            count_scissors +=1
        result = determine_winner(user_weapon, comp_weapon)
        # determine which sentence to output and count the number of rounds computer / user wins and ties
        if result == "comp_wins":
            outcome = result_comp_wins
            count_comp_wins +=1
        elif result == "user_wins":
            outcome = result_user_wins
            count_user_wins +=1
        else:
            outcome = result_tied
            count_tied +=1
        print "You have chosen %s and the computer chose %s." % (user_weapon, comp_weapon)
        print outcome + "\n"
        # keep prompting the user
        user_input = get_user_input()

    print "You quit the game!"
    print "The number of total rounds is %d." % (count_comp_wins + count_user_wins + count_tied)
    # determine singular or plural form
    comp_round = user_round = "rounds"
    if count_comp_wins == 1:
        comp_round = "round"
    if count_user_wins == 1:
        user_round = "round"
    print "The computer has won %d %s." % (count_comp_wins, comp_round)
    print "You have won %d %s." % (count_user_wins, user_round)
    print "The number of rounds that ended in a tie is %d." % (count_tied)
    # determine singular or plural form
    times_rock = times_paper = times_scissors = "times"
    if count_rock == 1:
        times_rock = "time"
    if count_paper == 1:
        times_paper = "time"
    if count_scissors == 1:
        times_scissors = "time"
    # output the number of times the user selected each weapon
    print "You chose Rock %d %s, Paper %d %s, Scissors %d %s." % (count_rock, times_rock, count_paper, times_paper, count_scissors, times_scissors)
    exit(0)

def get_user_input():
    user_input = raw_input("Please select your weapon: R/r for rock, P/p for paper, S/s for scissors, or Q/q to quit: ")
    return user_input


def choose_weapon():
    # randomly choose weapon: 1 for rock, 2 for paper, 3 for scissors
    import random
    number = random.randint(1,3)
    if number == 1:
        comp_weapon = "rock"
    elif number == 2:
        comp_weapon = "paper"
    else:
        comp_weapon = "scissors"
    return comp_weapon


def determine_winner(user_weapon, comp_weapon):
    # determine the winner
    if comp_weapon == "rock":
        if user_weapon == "rock":
            result = "tied"
        if user_weapon == "paper":
            result = "user_wins"
        if user_weapon == "scissors":
            result = "comp_wins"
    if comp_weapon == "paper":
        if user_weapon == "rock":
            result = "comp_wins"
        if user_weapon == "paper":
            result = "tied"
        if user_weapon == "scissors":
            result = "user_wins"
    if comp_weapon == "scissors":
        if user_weapon == "rock":
            result = "user_wins"
        if user_weapon == "paper":
            result = "comp_wins"
        if user_weapon == "scissors":
            result = "tied"
    return result

main()
