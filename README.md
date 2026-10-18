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

- [x] **Game purpose:** Game Glitch Investigator is a Streamlit number-guessing
  game. The player chooses Easy, Normal, or Hard, then uses higher/lower
  feedback to find a randomly selected number before running out of attempts.
  The game tracks guesses and score, and reveals the secret when the player
  wins or loses.
- [x] **Bugs found:** In the broken version, the secret could be regenerated
  during Streamlit reruns, making it seem to change between guesses. The
  higher/lower feedback was also unreliable: comparison and hint logic could
  disagree, including when the secret and guess were different types. The
  displayed guess range could be out of sync with the selected difficulty,
  and game state such as attempts or history was not consistently initialized
  or reset for a new round.
- [x] **Fixes applied:** The secret and other round data are now initialized
  in `st.session_state`, so rerunning the app preserves the secret, attempts,
  score, status, and history until a new game is started. Guess input is parsed
  into an integer and compared with the integer secret; the comparison returns
  the corresponding correct, too-high, or too-low hint. Difficulty-specific
  ranges and attempt limits are used in the interface, and **New Game** resets
  the round state and chooses a secret in the selected range. The reusable
  parsing, comparison, range, and scoring logic lives in `logic_utils.py` and
  is covered by the tests in `tests/test_game_logic.py`.

## 📸 Demo

### Demo Walkthrough

This walkthrough follows one complete game from the first screen to the win
message. The example uses **Normal** difficulty and assumes the randomly chosen
secret number is **42**. Your game will choose a different secret unless you
check the Developer Debug Info panel.

1. **Open the game.** The page is titled **Game Glitch Investigator**. In the
   sidebar, choose a difficulty: Easy, Normal, or Hard. Normal is selected by
   default. The selected difficulty sets the inclusive number range and the
   number of allowed attempts:

   | Difficulty | Guess range | Attempts |
   | --- | ---: | ---: |
   | Easy | 1–20 | 6 |
   | Normal | 1–100 | 8 |
   | Hard | 1–50 | 5 |

   The main page says **Make a guess** and shows the range and attempts left.
   With Normal selected, it starts at “Guess a number between 1 and 100.
   Attempts left: 8.” The **Show hint** checkbox is on by default.

2. **Check the example secret (optional).** Expand **Developer Debug Info** to
   see the current secret, attempts, score, difficulty, and guess history. In
   this example, the secret is 42, attempts are 0, score is 0, and history is
   empty. The secret stays the same while you submit guesses in this game.

3. **Make a guess that is too high.** Enter `60` and click **Submit Guess 🚀**.
   The app counts this as attempt 1, adds `60` to history, and displays the
   hint **“📉 Go LOWER!”** Since a wrong guess costs 5 points, the score
   changes from 0 to -5. The status remains in play and the page now shows
   7 attempts left.

4. **Make a guess that is too low.** Enter `30` and submit it. This is attempt
   2; history is now `[60, 30]`. The hint is **“📈 Go HIGHER!”** The score
   drops by another 5 points, from -5 to -10, and 6 attempts remain.

5. **Guess correctly.** Enter `42` and submit it. This is attempt 3, so the win
   is worth `100 - (10 × 3) = 70` points. Adding those points to the current
   score of -10 gives a final score of **60**. The app shows the “Correct!”
   hint, celebrates with balloons, and displays **“You won! The secret was
   42. Final score: 60.”** The status becomes won, so another submission will
   not start another round; the page instead says you already won and directs
   you to start a new game.

6. **Start another round.** Click **New Game 🔁** to reset attempts, score, and
   history, choose a new secret in the currently selected difficulty’s range,
   and return the status to playing. The app confirms **“New game started.”**
   Changing the difficulty updates the displayed range, attempt limit, and
   difficulty-specific guess input. It does not itself reset the current
   round’s secret, so click **New Game 🔁** after changing difficulty to start
   with a secret in the newly selected range.

**Input behavior:** Submitting a blank field displays **“Enter a guess.”**;
submitting non-numeric text displays **“That is not a number.”** Either
invalid submission still uses an attempt and appears as entered in history,
but does not change the score. Decimal text is converted to an integer by
truncating the fractional part (for example, `3.7` is treated as `3`).
Guesses are not otherwise restricted to the displayed range. Invalid
submissions do not trigger the out-of-attempts check, which is performed after
a valid, incorrect guess.

**If you use all your attempts without guessing correctly:** with Normal
difficulty, the eighth valid guess ends the game. The app reveals the secret
and shows **“Out of attempts!”** with the final score, then blocks further
guesses until you start a new game. Each valid wrong guess costs 5 points;
a correct guess earns `100 - (10 × attempt number)` points, with a minimum
win award of 10 points. If **Show hint** is unchecked, the higher/lower
warning is hidden, but guesses are still checked and scored as usual.

The walkthrough describes the game’s visible behavior; the Developer Debug
Info panel is there for investigating the game and is not needed to play.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
