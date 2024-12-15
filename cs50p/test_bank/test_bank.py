from bank import value


def test_bank_1():
    assert value('Hello') == 0
    assert value('hello, ben') == 0


def test_bank_2():
    assert value('hi!') == 20
    assert value('howdy, partner') == 20


def test_bank_3():
    assert value("What's up?") == 100
    assert value("What's happening?") == 100
