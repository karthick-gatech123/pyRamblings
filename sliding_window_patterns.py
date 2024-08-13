## fixed_window_size
def max_sum_subarray(nums, k):
  max_sum = 0
  window_sum = 0
  for i in range(0, k):
    window_sum += nums[i]
    max_sum = window_sum
    for i in range(k, len(nums)):
      window_sum += nums[i] - nums[i-k]
      max_sum = max(max_sum, window_sum)
  return max_sum

## dynamic_sliding_window
def min_subarray_len(nums, target):
  min_length = float("inf")
  window_sum = 0
  start = 0
  for end in range(0, len(nums)):
    window_sum += nums[end]
    while window_sum >= target:
      min_length = min(min_length, end - start + 1)
      window_sum -= nums[start]
      start += 1
  if min_length == float("inf"):
    return 0
    
  return min_length

# Caterpillar crawl solution
# note - below works only for positive numbers
def count_sub_arrays(nums, target):
  count = 0
  window_sum = 0
  start = 0
  for end in range(0, len(nums)):
    window_sum += nums[end]
    while window_sum > target:
      window_sum -= nums[start]
      start += 1
    if window_sum == target:
      count += 1
  return count

# some problems to practise for above approach
#
# - Number of Subarrays with Sum Equals K
# - Longest Subarray with Sum Less than or Equal to K
# - Subarray Product Less than K
