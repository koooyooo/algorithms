from A import find_index

def test_find_index():
    """
    解答が1パターン存在する場合は対象の Indexを昇順で返す
    """
    assert find_index([1, 3, 5, 7, 9], 6) == (0, 2)


def test_find_index_multi():
    """
    解答が2パターン存在する場合は最初に見つけたものを返す
    """
    assert find_index([1, 3, 5, 7, 9], 10) == (1, 3)

def test_no_answer():
    """
    解答が存在しない場合は -1, -1 を返す
    """
    assert find_index([1, 3, 5, 7, 9], 99) == (-1, -1)