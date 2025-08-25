

def find_index(nums: list[int], target: int) -> tuple[int, int]:
    hash = {}
    for i, num in enumerate(nums):
        tgt = target - num
        if tgt in hash:
            return (hash[tgt], i)
        else:
            hash[num] = i
    return (-1, -1)


def main():
    ans = find_index([1, 3, 5, 7, 9], 6)
    print(ans)
    assert ans == (0, 2)


if __name__ == "__main__":
    main()
