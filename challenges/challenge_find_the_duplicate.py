from challenges.merge_sort import merge_sort


def validate_nums(nums, list_size):
    if nums[0] < 0 or list_size < 1:
        raise ValueError


def find_duplicate(nums):
    target = 0
    next_target = 1

    try:
        list_size = len(nums)

        merge_sort(nums)
        validate_nums(nums, list_size)

        for _ in range(list_size):
            if nums[target] == nums[next_target]:
                return nums[target]
            else:
                move = 1
                target += move
                next_target += move

    except (TypeError, IndexError, ValueError):
        pass

    return False
