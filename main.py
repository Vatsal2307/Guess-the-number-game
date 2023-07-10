#Number Guessing Game Objectives:
from art import logo
import random
print(logo)

print("I am guessing a number between 1 to 100")

def game_play(diff_level):
  
  def lev_easy(): 
    total_attempts = 10
    while total_attempts != 0:
      user_inp = int(input("Make a guess "))
      if user_inp > number:
        print("Too high")
        total_attempts = total_attempts -1
        print(f"You have {total_attempts} attempts left to guess the answer. ")
      elif user_inp < number:
        print("Too low")
        total_attempts = total_attempts -1
        print(f"You have {total_attempts} attempts left to guess the answer. ")
      elif user_inp == number:
        print(f"You win! with {total_attempts} attempts left to spare. ")
        total_attempts = 0
        
        
  def lev_hard():
    print("You have 5 attempts to guess the number ")
    total_attempts = 5
    while total_attempts != 0:
      user_inp = int(input("Make a guess "))
      if user_inp > number:
        print("Too high ")
        total_attempts = total_attempts -1
        print(f"You have {total_attempts} attempts left to guess the answer. ")
      elif user_inp < number:
        print("Too low ")
        total_attempts = total_attempts -1
        print(f"You have {total_attempts} attempts left to guess the answer. ")
      elif user_inp == number:
        print(f"You win! with {total_attempts} attempts left to spare. ")
        total_attempts = 0
           
  if diff_level == "easy":
    lev_easy()
  elif diff_level == "hard":
    lev_hard()

number = random.randint(1,100)
print(f"Correct answer is {number}")
diff_level = input("Choose a difficulty level. Type 'easy' or 'hard'")
if diff_level == "easy":
  game_play(diff_level = "easy")
   
elif diff_level == "hard":
  game_play(diff_level= "hard")

  

