from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score


# --- check_guess tests ---

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_message_when_too_high():
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message

def test_hint_message_when_too_low():
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message


# --- get_range_for_difficulty tests ---

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 50)

def test_unknown_difficulty_defaults():
    assert get_range_for_difficulty("Unknown") == (1, 100)


# --- parse_guess tests ---

def test_parse_valid_int():
    ok, val, err = parse_guess("42")
    assert ok is True
    assert val == 42
    assert err is None

def test_parse_float_string():
    ok, val, err = parse_guess("3.7")
    assert ok is True
    assert val == 3

def test_parse_empty_string():
    ok, val, err = parse_guess("")
    assert ok is False
    assert val is None

def test_parse_none():
    ok, val, err = parse_guess(None)
    assert ok is False

def test_parse_non_numeric():
    ok, val, err = parse_guess("abc")
    assert ok is False
    assert "not a number" in err.lower()


# --- update_score tests ---

def test_score_on_win_first_attempt():
    score = update_score(0, "Win", 1)
    assert score == 90

def test_score_on_win_late_attempt():
    score = update_score(0, "Win", 10)
    assert score == 10  # minimum 10 points

def test_score_penalty_on_wrong_guess():
    score = update_score(100, "Too High", 1)
    assert score == 95
    score = update_score(100, "Too Low", 2)
    assert score == 95
