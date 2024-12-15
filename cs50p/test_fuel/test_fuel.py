import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("2/3") == 67
    assert convert("1/1") == 100
    assert convert("0/1") == 0
    with pytest.raises(ValueError):
        assert convert("a/b")
    with pytest.raises(ValueError): #you shouldn't have to check for this if the code is right
        assert convert("5/2")
    with pytest.raises(ZeroDivisionError): # and for this as well
        assert convert("0/0")



def test_gauge():
    assert gauge(33) == "33%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
