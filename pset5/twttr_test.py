from twttr import shorten

def test_lowercase():
    assert shorten('twitter') == 'twttr'

def test_uppercase():
    assert shorten('TWITTER') == 'TWTTR'

def test_titlecase():
    assert shorten('Twitter') == 'Twttr'

def test_mixedcase():
    assert shorten('TwItTEr') == 'TwtTr'