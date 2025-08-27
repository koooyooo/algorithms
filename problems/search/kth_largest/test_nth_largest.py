from dataclasses import dataclass
import pytest

# N番目に大きな数を取得する
def nth_largest(nums: list[int], k: int, distinct: bool = False) -> int:
    """
    N番目に大きな数を取得する。
    """
    if distinct:
        nums = list(set(nums))
    sorted_unique_nums = sorted(nums)
    return sorted_unique_nums[-k]


@pytest.mark.parametrize("nums,k,distinct,expected", [
    ([3, 2, 1, 5, 6, 4], 2, True, 5),
    ([7, 10, 4, 3, 20, 15], 3, True, 10),
    ([5, 5, 4], 2, True, 4),
    ([5, 5, 4], 2, False, 5),
    ([-5, -2, -3], 2, True, -3),
    ([0], 1, True, 0),
])

def test_basic(nums, k, distinct, expected):
    assert nth_largest(nums, k, distinct) == expected
