from game_data import data
import random
from replit import clear
from art import logo, vs

def get_random():
  return random.choice(data)

def format_data(account):
  name = account['name'] 
  description = account['description']
  country = account["country"]

  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_follower, b_follower):
  if a_follower > b_follower:
    return guess == "a"
  else:
    return guess == "b"  

def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_b = get_random()
  
  while game_should_continue:
    account_a = account_b 
    account_b = get_random()

    while account_b == account_a:
      account_b = get_random()

    print(f"Compare A: {format_data(account_a)}") 
    print(vs)   
    print(f"Against B: {format_data(account_b)}") 

    guess = input("Who has more follers? Type 'a' or 'b'? :  ").lower()

  
    is_correct = check_answer(guess, account_a['follower_count'], account_b['follower_count'])

    clear()
    print(logo)

    if is_correct:
      score += 1
      print(f"You are right! Current score:  {score}")
    else:
      game_should_continue = False
      print(f"Sorry! Final score:  {score}")
    # clear()
    # print(logo)
game()




