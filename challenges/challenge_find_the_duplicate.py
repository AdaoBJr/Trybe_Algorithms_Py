def find_duplicate(nums):
    for item in nums:
        if not isinstance(item, int):
            return False
        if item < 0:
            return False
        if nums.count(item) >= 2:
            return item
    return False