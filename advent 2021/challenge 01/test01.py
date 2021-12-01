from number01 import process_depth


def test_first_result():
    increase = process_depth([int(f.strip('\n')) for f in open('./test_input.txt').readlines()])
    assert increase == 7


def test_second_result():
    increase = process_depth([int(f.strip('\n')) for f in open('./test_input.txt').readlines()], use_sliding_window=True)
    assert increase == 5

