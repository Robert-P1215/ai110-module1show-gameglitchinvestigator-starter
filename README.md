# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Game starts with correct number of guesses, and difficulty on left, automatically resetting game to conform to rules of selected difficulty.
2. Players can guess number between specified ranges and the game will say higher or lower.
3. Players can restart game whenever they want as many times as needed.
4. Players will correctly be given hints can can guess the correct number to win, otherwise they lose with guesses being marked right and wrong correctly.
5. Game can reset upon victory/loss as needed.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
===================================================================================================================== test session starts =====================================================================================================================
platform win32 -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\Robert\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 21 items                                                                                                                                                                                                                                             

tests\test_game_logic.py .....................                                                                                                                                                                                                           [100%]

===================================================================================================================== 21 passed in 0.07s ======================================================================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
