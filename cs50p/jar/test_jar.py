import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12
    jar = Jar(20, 10)
    assert jar.size == 10
    assert jar.capacity == 20


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12
    jar.deposit()
    assert str(jar) == "🍪"
    jar.deposit(4)
    assert jar.size == 5
    with pytest.raises(ValueError):
        assert jar.deposit(13)


def test_withdraw():
    jar = Jar(12, 12)
    assert jar.size == 12
    assert jar.capacity == 12
    jar.withdraw()
    assert jar.size == 11
    jar.withdraw(4)
    assert jar.size == 7
    with pytest.raises(ValueError):
        assert jar.withdraw(8)
