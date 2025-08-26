# N番目に大きな数を取得する
def nth_largest(nums: list[int], k: int) -> int:
    unique_nums = list(set(nums))
    sorted_unique_nums = sorted(unique_nums)
    return sorted_unique_nums[-k]

def test_nth_largest():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert nth_largest(nums, k) == 5

    nums = [7, 10, 4, 3, 20, 15]
    k = 3
    assert nth_largest(nums, k) == 10

