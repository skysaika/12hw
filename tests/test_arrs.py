from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([1, 2, 3, 4], 3, "test") == 4
    assert arrs.get([], -2, "test") == "test"
    assert arrs.get([1, 2], 1, "test") == 2
    assert arrs.get([], -5, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -5) == [1, 2, 3]
    assert arrs.my_slice([], -1) == []