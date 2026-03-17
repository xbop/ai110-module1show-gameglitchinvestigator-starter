# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- When in "Normal" mode, I kept getting the same hint to go lower no matter how low I went. I would expect the game to accurately determine whether the correct answer is higher or lower than my inputted guess.
- When in "Easy" mode, I kept getting the same hint to go higher no matter how high I went. I would expect the game to accurately determine whether the correct answer is higher or lower than my inputted guess.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). Saying to swap the "Go Lower" and "Go Higher" messages.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). Saying to convert variables to string when it should've been int.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? Tested it live on the site and made sure to account for edge cases.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. I reran the "Normal" level and was able to effectively play and eventually guess the correct answer.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app. The secret number's value stays the same, but the version of it passed into check_guess alternates between int and str every attempt. Since comparing an int to a string produces completely different results than comparing two ints, the game's responses are inconsistent.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?  Streamlit works very differently from a traditional app. Every single time you interact with anything such as clicking a button, typing in a box, or changing a dropdown, Streamlit reruns your entire script from top to bottom. That means any normal Python variable like `secret = random.randint(1, 100)` would be reassigned to a fresh random number on every click.

- What change did you make that finally gave the game a stable secret number? The fix is removing the str() conversion so the secret is always compared as a plain integer.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? Verifying the fix was actually implemented rather than blindly trusting the AI.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task? Implementing changes before planning and checking logic across multiple LLMs.
- In one or two sentences, describe how this project changed the way you think about AI generated code. The code accuracy benefits from the specificity of the prompt, the depth of the context, and the direct wayfinding to the error (as identified by the developer).
