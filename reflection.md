# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
-Entering guesses would cause the opposite hint to be given to the user. (higher would prompt lower and vice versa)
-The new game button does not refresh hints and does not correctly restart the game.
-When swapping modes, the secret number does not update automatically to the new criteria.
-On even attempts, the game would act strangely at times

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.



| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
guess 10 (secret is 5)| hint given is too high| hint given is too low| None
pressing new game after ending| level restarts, messages cleared, states reset| game is stuck and would not restart|Game over. Start a new game to try again.
swapped to a different difficulty| new secret number is generated within the new criteria| old secret number retained, did not update| None
on even attempts, correct guess is input| game ends with victory| sometimes, the guess is marked wrong| None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Used Claude code and ChatGPT with Gemini on mobile
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - ChatGPT suggested that the logic of the return statements could potentially be correct, but have their messages swapped due to logical mistake. I located the relevant code and found that it was indeed as ChatGPT theorized and made the necessary switch. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - Gemini suggested that the difficulty tracker had already been made and that the logic error was actually within the start game button. While the start game button did have an error, Gemini was incorrect in its assumption that the difficulty was being stracked in a session state.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - A bug was fixed once the pytest case was a succes and i had manually attempted to recreate the bug in the updated game.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - One of the manual tests i did was to keep trying guesses that were either too high and too low to see what the pattern of the issue was, and then reattempting once the code had been swapped.
- Did AI help you design or understand any tests? How?
  - Ai helped me design many of the pytest cases and created another file called conftest.py which resolved an import statement error with the pytest file.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
