# Created import and conftest.py and pytest cases with AI to test functionallity of corrected code, also modified existing test cases
from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == 'Win'

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


# --- Bug 1: Opposite hints (high/low reversed) ---

def test_high_guess_gives_go_lower_message():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_low_guess_gives_go_higher_message():
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_guess_one_above_secret_is_too_high():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"

def test_guess_one_below_secret_is_too_low():
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"


# --- Bug 2: New game resets state — check_guess and update_score are pure ---

def test_score_starts_at_zero_win_first_attempt():
    score = update_score(0, "Win", 1)
    assert score > 0

def test_fresh_secret_correct_guess_wins():
    outcome, _ = check_guess(37, 37)
    assert outcome == "Win"

def test_non_win_outcome_does_not_award_win_points():
    too_high_score = update_score(0, "Too High", 1)
    win_score = update_score(0, "Win", 1)
    assert too_high_score != win_score


# --- Bug 3: Secret must fit the new difficulty range on mode swap ---

def test_easy_range_is_1_to_20():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range_is_1_to_100():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range_is_1_to_50():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_secret_above_easy_max_is_not_reachable():
    # 25 is outside Easy range (1-20); guessing 20 should still be Too Low
    outcome, _ = check_guess(20, 25)
    assert outcome == "Too Low"

def test_all_easy_secrets_are_winnable():
    for secret in range(1, 21):
        outcome, _ = check_guess(secret, secret)
        assert outcome == "Win"


# --- Bug 4: Even attempts returned string secret causing wrong comparisons ---

def test_check_guess_with_string_secret_correct():
    outcome, _ = check_guess(42, "42")
    assert outcome == "Win"

def test_check_guess_with_string_secret_too_high():
    outcome, _ = check_guess(80, "50")
    assert outcome == "Too High"

def test_check_guess_with_string_secret_too_low():
    outcome, _ = check_guess(20, "50")
    assert outcome == "Too Low"

def test_check_guess_both_string_inputs():
    outcome, _ = check_guess("42", "42")
    assert outcome == "Win"

def test_parse_guess_returns_int():
    ok, value, _ = parse_guess("7")
    assert ok is True
    assert isinstance(value, int)

def test_parse_guess_float_string_returns_int():
    ok, value, _ = parse_guess("7.9")
    assert ok is True
    assert isinstance(value, int)
    assert value == 7
