# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Submit an integer guess on an even-numbered attempt | Compare the guess and secret numerically | The secret was converted to a string; the fallback compared digit strings lexicographically, so the hint could be wrong | The `TypeError` was caught; no error was shown in the app |
| Guess above the secret (for example, 60 when the secret is 50) | Show “Go LOWER!” | The game showed “Go HIGHER!” | None |
| Start a new game after changing to Easy | Choose and display a secret in the 1–20 range | The displayed range stayed 1–100, and the new secret was chosen from 1–100 | None |

- When in "Normal" mode, I kept getting the same hint to go lower no matter how low I went. I would expect the game to accurately determine whether the correct answer is higher or lower than my inputted guess.
- When in "Easy" mode, I kept getting the same hint to go higher no matter how high I went. I would expect the game to accurately determine whether the correct answer is higher or lower than my inputted guess.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). It suggested swapping the “Go Lower” and “Go Higher” messages. I verified the change by testing guesses above and below the secret and confirming each hint pointed toward it.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). The suggestion to convert the secret to a string was not appropriate: it caused numeric comparisons to fail and the fallback compared strings lexicographically. I kept both values as integers and verified the comparison and hint behavior with tests and a live game.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? Tested it live on the site and made sure to account for edge cases.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. I reran the "Normal" level and was able to effectively play and eventually guess the correct answer.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? Streamlit reruns the script from top to bottom after interactions such as clicking a button or changing a selection. Regular local variables are recreated during that rerun, while values stored in `st.session_state` persist for that user's session.
- The secret itself did not change on every rerun because it was already kept in session state. The bug was that every other guess passed it to `check_guess` as a string instead of an integer, which led to incorrect comparisons and hints. Keeping both values as integers fixed the comparison.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? Verifying the fix was actually implemented rather than blindly trusting the AI.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task? Implementing changes before planning and checking logic across multiple LLMs.
- In one or two sentences, describe how this project changed the way you think about AI generated code. The code accuracy benefits from the specificity of the prompt, the depth of the context, and the direct wayfinding to the error (as identified by the developer).
