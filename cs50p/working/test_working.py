import pytest

from working import convert


def test_convert_1():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('12 PM to 12 AM') == '12:00 to 00:00'
    assert convert('8 AM to 8 AM') == '08:00 to 08:00'
    assert convert('9 PM to 5 PM') == '21:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'


def test_convert_2():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('12:00 PM to 12:00 AM') == '12:00 to 00:00'
    assert convert('8:00 AM to 8:00 AM') == '08:00 to 08:00'
    assert convert('9:00 PM to 5:00 PM') == '21:00 to 17:00'
    assert convert('10:00 PM to 8:00 AM') == '22:00 to 08:00'


def test_convert_wrong_format():
    with pytest.raises(ValueError):
        assert convert('9 AM - 5 PM')
        assert convert('"9:00 AM 5:00 PM"')
        assert convert('"9 AM 5 PM"')
        assert convert('9AM to 5PM')
        

def test_convert_wrong_hours():
    with pytest.raises(ValueError):
        assert convert('13 AM to 17 PM')
        assert convert('13:00 AM to 17:00 PM')
        assert convert('13 PM to 17 PM')
        assert convert('21:00 to 17:00')
        assert convert('09 AM to 09 PM')


def test_convert_wrong_minutes():
    with pytest.raises(ValueError):
        assert convert('12:65 AM to 11:82 PM')
        assert convert('8:60 AM to 4:60 PM')

