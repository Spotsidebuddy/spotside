from numb3rs import validate


def test_numb3rs_correct_nums():
    assert validate('255.255.255.255')
    assert validate('0.0.0.0')
    assert validate('127.0.0.1')


def test_numb3rs_words():
    assert not validate('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
    assert not validate('cat')
    assert not validate('127.cat.0.2')
    assert not validate('127.0.cat.2')
    assert not validate('127.0.0.cat')


def test_numb3rs_incorrect_values():
    assert not validate('-2.12.32.15')
    assert not validate('256.256.256.256')
    assert not validate('2.-1.11.50')
    assert not validate('2.12.32.-15')
    assert not validate('2.300.32.15')


def test_numb3rs_incorrect_length():
    assert not validate('10.10.10.10.10')
    assert not validate('10.10.10')

