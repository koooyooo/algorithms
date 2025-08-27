from dataclasses import dataclass

# N番目に大きな数を取得する
def nth_largest(nums: list[int], k: int) -> int:
    unique_nums = list(set(nums))
    sorted_unique_nums = sorted(unique_nums)
    return sorted_unique_nums[-k]

# Test
@dataclass
class Scenario:
    input_data: dict
    expected: int
    description: str = ""

def test_nth_largest():
    test_cases: list[Scenario] = [
        Scenario({"nums": [3, 2, 1, 5, 6, 4], "k": 2}, 5, "基本的なケース"),
        Scenario({"nums": [7, 10, 4, 3, 20, 15], "k": 3}, 10, "重複なしの配列"),
        Scenario({"nums": [1, 1, 1, 1], "k": 1}, 1, "重複のみの配列"),
        Scenario({"nums": [5], "k": 1}, 5, "単一要素"),
        Scenario({"nums": [3, 3, 3, 3, 3], "k": 1}, 3, "同じ値のみ"),
    ] 

    for test_case in test_cases:
        result = nth_largest(test_case.input_data["nums"], test_case.input_data["k"])
        assert result == test_case.expected, f"Failed: {test_case.description} - Expected {test_case.expected}, got {result}"


if __name__ == "__main__":
    test_nth_largest()
    print("All tests passed!")
    