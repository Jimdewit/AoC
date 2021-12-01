from number04 import check_sizes


def test_valid_result():
    valid, double, treble = check_sizes(112255)
    assert double


def test_invalid_result():
    valid, double, treble = check_sizes(319877)
    assert not valid


def test_invalid_treble():
    valid, double, treble = check_sizes(1233345)
    assert treble
