nums = [2, 7, 3, 1, 7]

# Python実装
def test_2nd_largest():
    v_2nd = max([v for v in nums if v != max(nums)])
    assert v_2nd == 3

# 自作
def test_2nd_largest_2():
    v_1st, v_2nd = 0, 0
    for num in nums:
        prev_1st = v_1st
        if v_2nd < num and v_1st < num:
            v_1st = num
            v_2nd = max(v_2nd, prev_1st)
        if v_2nd < num and num < v_1st:
            v_2nd = num
    assert v_2nd == 3

# 模範解答
def test_2nd_largest_3():
    v_1st, v_2nd = float('-inf'), float('-inf')
    for num in nums:
        if num > v_1st:
            v_1st = num
        elif v_1st > num and num > v_2nd:
            v_2nd = num
    assert v_2nd == 3
