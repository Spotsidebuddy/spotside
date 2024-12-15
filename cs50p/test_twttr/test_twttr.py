from twttr import shorten


def test_shorten_lower():
    assert shorten('heck') == 'hck'
    assert shorten('USING BIG WORDS NOW') == 'SNG BG WRDS NW'
    assert shorten('CaMeL tExT tEsT') == 'CML txT tsT'
    assert shorten('Only bIg vOwEls') == 'nly bg vwls'
    assert shorten('oNLY BiG CoNSoNaNTS') == 'NLY BG CNSNNTS'
    assert shorten('Hit me!') == 'Ht m!'
    assert shorten('2 good 2 be true') == '2 gd 2 b tr'

