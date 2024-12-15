from seasons import compute
import pytest


def test_compute_correct():
    assert compute('2023', '05', '13') == 527040
    assert compute('2022', '05', '13') == 1052640

def test_compute_future():
    with pytest.raises(SystemExit):
        assert compute('2030', '12', '01')

def test_compute_invalid_format():
    with pytest.raises(SystemExit):
        assert compute('Jan 12, 1986', '', '')
