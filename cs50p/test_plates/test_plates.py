from plates import is_valid

def test_cond_1():
  # All vanity plates must start with at least two letters
    assert is_valid('AA2222') == True
    assert is_valid('A22222') == False
    assert is_valid('230AVS') == False
    assert is_valid('ABCDEF') == True

def test_cond_2():
    # Vanity plates may contain a maximum of 6 characters (letters or numbers)
    # and a minimum of 2 characters
    assert is_valid('AA') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFG') == False
    assert is_valid('ABCD0123') == False

def test_cond_3():
    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # AAA222 would be an acceptable vanity plate;
    # AAA22A would not be acceptable.
    # The first number used cannot be a '0'
    assert is_valid('AA0234') == False
    assert is_valid('AA1234') == True
    assert is_valid('AA133D') == False

def test_cond_4():
    # No periods, spaces, or punctuation marks are allowed
    assert is_valid('!FCUK') == False
    assert is_valid('AA2!') == False
    assert is_valid('ABCD@E') == False
