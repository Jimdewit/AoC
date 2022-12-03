from number15 import solve


def test_valid_result():
    outcome = solve([f.strip('\n') for f in open('./test_input.txt').readlines()])
    assert outcome == 1


def test_invalid_result():
    outcome = solve([f.strip('\n') for f in open('./test_input.txt').readlines()])
    assert outcome != 1