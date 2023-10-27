# Faculty of Information
# University of Toronto
# BI program
# Course: INF452
# Instructor: Dr. Maher Elshakankiri
# Name: Julie Nguyen
# Assignment: 2.1
# Date Create: October 03, 2023
# Last Modified: October 05, 2023

# Hangman game
import random as rd
import turtle as tt

# Set up drawing
def drawHangman(attempts):
    draw = [(tt.pendown(), tt.forward(500)), # Base 1
        (tt.right(90), tt.forward(200)), # Base 2
        (tt.right(90), tt.forward(100)), # Base 3
        (tt.penup(), tt.right(180), tt.goto(30,0), tt.pendown(), tt.circle(30), tt.penup()), # Head
        (tt.goto(0,-30), tt.right(180), tt.pendown(), tt.forward(150)), # Body
        (tt.goto(0, -70), tt.pendown(), tt.right(45), tt.forward(40), tt.penup()), # Left hand
        (tt.goto(0, -70), tt.pendown(), tt.right(270), tt.forward(40), tt.penup()), # Right hand
        (tt.goto(0, -180), tt.pendown(), tt.right(90), tt.forward(40), tt.penup()), # Left leg
        (tt.goto(0, -180), tt.pendown(), tt.right(270), tt.forward(40), tt.penup())]
    for i in range(attempts):
        for k in draw[i]:
            k
    tt.done()

    if attempts == len(draw):
        print("You lose!")
    

# Choose difficulty
def chooseDifficulty():
    difficulty = int(input("Choose your difficulty: "))
    if difficulty == 1:
        print("Easy")
    elif difficulty == 2:
        print("Medium")
    else:
        print("Hard")
    return chooseDifficulty


# Choose word
def chooseWord():
    word_bank = ["apple", "banana", "elephant", "pineapple"]
    return rd.choice(word_bank)

# Main game 
print("Hi! Welcome to Hangman!")

tt.pensize(5)
tt.penup()
tt.goto(-200, -200)
tt.left(90)

guessed_items = []

original_word = chooseWord()
attempts = 0
for letter in original_word:
    print("_ ", end="")
while attempts < len(draw):
    guessed_letter = input("Enter a letter: ").lower() # Case insensitive

    if len(guessed_letter) != 1 or guessed_letter.isalpha():
        input("Invalid input. Please enter a valid single letter: ")
        continue

    if guessed_letter in guessed_items:
        input("You already guessed this letter. Try again: ")
        continue

    guessed_items.append(guessed_letter)

    if guessed_letter in original_word:
        for i in range(len(original_word)):
            if guessed_letter == original_word[i]:
                print(original_word[i],end="")
            else:   
                print("_",end="")
    else:
        attempts += 1
        drawHangman(attempts)
                    
tt.done()