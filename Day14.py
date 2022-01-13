from Data import data
import random


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"



def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
        
        
    print(f"compare A: {format_data(account_a)}")
    print(f"Against B: {format_data(account_b)}")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()


    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score +=1
        print(f"You are Right, your final score is {score}")
    else:
        print(f"Sorry, that's wrong, your final score is {score}")
        game_should_continue = False