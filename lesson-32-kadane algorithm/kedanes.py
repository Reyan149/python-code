def max_sub_array_brute_force(nums):
    n = len(nums)
    maxi = float('-inf')
    start_idx = 0
    end_idx = 0

    for i in range(0, n):
        total = 0
        for j in range(i, n):
            total = total + nums[j]

            if total > maxi:
                maxi = total
                start_idx = i
                end_idx = j

    best_subbarray = nums[start_idx:end_idx + 1]
    
    return maxi, best_subbarray, start_idx, end_idx

sample_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray, start, end = max_sub_array_brute_force(sample_nums)
print(f"Maximum subarray sum: {max_sum}")
print('The Subarray:', subarray)
print(f'Found from index {start} to {end}')