

def find_index(nums: list[int], target: int) -> tuple[int, int]:
    hash = {}
    for i, num in enumerate(nums):
        tgt = target - num
        if tgt in hash:
            return (hash[tgt], i)
        else:
            hash[num] = i
    return (-1, -1)

