import art
import random

print(art.logo)
play_blackjack = input("Would you like to play a game of blackjack? type 'y' for yes, or 'n' for no. ")

if play_blackjack == "y":
    play_blackjack = True
elif play_blackjack == "n":
    play_blackjack = False

while play_blackjack:

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #Standard Blackjack Deck
    user = []
    computer = []

    def deal_card():
        """Deals a single card from the deck."""
        card = random.choice(cards)
        return card

    def calculate_score(hand):
        """Calculates the score of a hand, treating Aces as 11 unless it is a bust."""
        total = 0
        ace_count = hand.count(11)
        for card in hand:
            if card == 11:
                total+= 11
            else:
                total += card

        while total > 21 and ace_count > 0: #Adjust for Aces
            total -= 10
            ace_count -= 1
        return total

    #Deal Hands
    user_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]

    #Prints the hands
    print(f"Your hand: {user_hand}, your score is: {calculate_score(user_hand)}")
    print(f"Computers first card: {computer_hand[0]}, computers score is: Hidden")

    if calculate_score(user_hand) == 21:
        print("You got Blackjack! You Win!")
        play_blackjack = False
    elif calculate_score(user_hand) > 21:
        print("You got more than 21. You Lose!")
        play_blackjack = False
    elif calculate_score(computer_hand) == 21:
        print("Computer got Blackjack! You Lose!")
        play_blackjack = False
    else:
        while calculate_score(user_hand) < 21:
            print("your current hand value is:", calculate_score(user_hand))
            choice = input("Hit or Stand? ").lower()
            if choice == "hit":
                user_hand.append(deal_card())
                calculate_score(user_hand)
            elif choice == "stand":
                break #Exit loop for the user choosing to stand
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")

        if calculate_score(computer_hand) <= 21:
            print("Computer's turn...")
            while calculate_score(computer_hand) < 17:
                computer_hand.append(deal_card())
                calculate_score(computer_hand)
        print(f"your final hand: {user_hand}, your score: {calculate_score(user_hand)}")
        print(f"computers final hand: {computer_hand}, computers score: {calculate_score(computer_hand)}")

        if calculate_score(computer_hand) > 21:
            print("Computer busted!, you Win!")
            play_blackjack = False
        elif calculate_score(user_hand) > 21:
            print("You Busted!, You Lose!")
            play_blackjack = False
        elif calculate_score(user_hand) > calculate_score(computer_hand):
            print("You Win!")
            play_blackjack = False
        elif calculate_score(user_hand) < calculate_score(computer_hand):
            print("You Lose!")
            play_blackjack = False
        else:
            print("It's a Tie")
            play_blackjack = False

    play_again = False
    while True:  # Play again loop
        answer = input("Would you like to play another hand of blackjack? type 'y' for yes, or 'n' for no. ")
        if answer == "y":
            play_again = True
            play_blackjack = True
            break  # Exit the inner loop
        elif answer == "n":
            print("Thanks for playing!")
            break  # Exit the inner loop
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    if not play_again:
        break  # Exit the outer loop, ending the program
