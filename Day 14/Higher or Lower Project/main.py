#Import art and modules needed
from art import logo, vs
from game_data import data
import random

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0

game_continue = True

b_account = random.choice(data)

while game_continue:
    a_account = b_account
    b_account = random.choice(data)

    if a_account == b_account:
        b_account = random.choice(data)

    print(f"Compare A: {format_data(a_account)}")
    print(vs)
    print(f"Against B: {format_data(b_account)}")

    guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = a_account["follower_count"]
    b_follower_count = b_account["follower_count"]

    is_correct = check_answer(user_guess=guess, a_followers=a_follower_count, b_followers=b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False


