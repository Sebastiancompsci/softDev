""" Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
"""


def array_front9(nums):
  return (nums[:3].count(9) >= 1)

print(array_front9([1, 2, 9, 3, 4])) # → True
print(array_front9([1, 2, 3, 4, 9])) # → False
print(array_front9([1, 2, 3, 4, 5])) # → False

