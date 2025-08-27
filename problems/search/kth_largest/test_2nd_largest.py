# Python実装
def second_largest_python(nums: list[int]) -> int:
    return max([v for v in nums if v != max(nums)])

# 個人実装
def second_largest_mine(nums: list[int]) -> int:
    v_1st, v_2nd = 0, 0
    for num in nums:
        prev_1st = v_1st
        if v_2nd < num and v_1st < num:
            v_1st = num
            v_2nd = max(v_2nd, prev_1st)
        if v_2nd < num and num < v_1st:
            v_2nd = num
    return v_2nd

# 模範解答
def second_largest_ans(nums: list[int]) -> int:
    v_1st, v_2nd = float('-inf'), float('-inf')
    for num in nums:
        if num > v_1st:
            v_1st = num
        elif v_1st > num and num > v_2nd:
            v_2nd = num
    return v_2nd

# Test
def test_2nd_largest():
    nums = [2, 7, 3, 1, 7]
    for f in [second_largest_python, second_largest_mine, second_largest_ans]:
        assert f(nums) == 3
