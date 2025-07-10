

# 🕹️ B* You Guessed It – Number Guessing Game

A beginner-friendly Python terminal game where the user has to guess a randomly generated number within a limited number of attempts.

---

## 🚀 Project Overview

**You Guessed It** is a simple CLI (Command Line Interface) game built using Python. The program selects a secret number between 1 and 30, and the user has 9 attempts to guess it correctly. 
After each guess, the program tells the user whether the guess was too high or too low.

This project was created as part of the **Melanated Machine Learning (MML)** journey and is one of the first interactive Python games in the learning portfolio.

---
## 🧠 Learning Concepts

- `random.randint()` usage
- Flow control: `if`, `elif`, `else`
- Loops: `while`
- User input with `input()`
- Basic debugging and logic structuring

---

## 📁 Project Structure
- `youGuessedIt.py` – Main Python script
- `README.md` – Project documentation

---

## ⚙️ Requirements
- Python 3.x installed
- Text editor or IDE (VS Code, PyCharm, etc.)

---

## 💻 How to Run/Use 

1. Make sure you have Python installed (Check with: python3 --version)
2. Save the game file as `youGuessedIt.py`
3. Open the file in your preferred editor (e.g., VS Code)
4. Open your terminal and navigate tot he project folder  
5. Run the script using:
```bash
python3 youGuessedIt.py

# B* You Guessed It . The Number's Game...

import random 
secretNumber = random.randint(1, 30 )
print("I am thinking of a number between 1 and 30")

#Ask the player to guess 9 times.
for guessesTaken in range(1, 10): 
    print("Take a guess.")
    guess = int(input()) 

    if guess < secretNumber: 
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else: 
        break  #This Condition is the correct guess ! 

if guess == secretNumber:
    print("B* You Guessed It! Only took " + str(guessesTaken) + " tries.") 
else: 
    print("Too Bad. The number was " + str(secretNumber)) 



```
<! --- --- --- >
B* You Guessed It 

---

## 🔮 Future Additions 
  - Difficulty levels (easy, medium, hard)
  - Score tracker / performance stats
  - UI version (Tkinter or web-based)
  - Voice-activated guesses (for accessibility)

---

## 📄 License
  - https://choosealicense.com/licenses/mit/ 
- This project is licensed under the MIT License. Feel free to use and modify it!

---

## 🧠 Author

- Built by Q aka Groovy Woo — documenting the learning journey publicly through the Melanated Machine Learning (MML) project.
- Visit *MML GitHub* and follow along.

---

## 📌 Project Status

- ✅ Version 1 Complete
- 🚧 Version 2 In Planning (score tracking + difficulty levels)


