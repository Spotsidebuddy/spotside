from um import count


def test_count_corner_cases():
    assert count('') == 0
    assert count('Mum!') == 0
    assert count('umami') == 0
    assert count('yummi!') == 0
    assert count('umm') == 0


def test_normality():
    assert count('um') == 1
    assert count('Um, what, um?..') == 2
    assert count('Its, um... Easy!') == 1


def test_mixed():
    assert count('Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?') == 2
    assert count('Um, umami is not the favourite, um... Taste of alumni') == 2
