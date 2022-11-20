def has_negative_number(nums):
    if nums[0] < 0:
        raise ValueError


def check_size(nums):
    list_size = len(nums)
    if list_size < 1:
        raise ValueError

    return list_size


def find_duplicate(nums):
    try:
        nums.sort()
        list_size = check_size(nums)
        has_negative_number(nums)

        for index in range(list_size - 1):
            if nums[index] == nums[index + 1]:
                return nums[index]

    except (TypeError, ValueError):
        pass

    return False
