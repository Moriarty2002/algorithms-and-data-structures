from sys import maxsize as ms

def max_subarray(nums, n: int = None, memoized_optimal: list = None):
    is_first_call = False
    
    if n is None: # First call init
        n = len(nums) - 1 
        memoized_optimal = [None for _ in range(n+1)] 
        is_first_call = True

    
    if not n: # base case with subsequence of length n
        memoized_optimal[0] = nums[0]
        return nums[0]
    
    if memoized_optimal[n] is not None:
        return memoized_optimal[n]
    
    # Recursivamente trova la somma massima che termina in n
    memoized_optimal[n] = max(nums[n], nums[n] + max_subarray(nums, n - 1, memoized_optimal))
    
    if is_first_call:
        return max(memoized_optimal)
    
    return memoized_optimal[n]
    

nums = [4, -1, 2, 1, -5, 4]
print(f"Max subsequence for {nums} is: {max_subarray(nums)}" )

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Max subsequence for {nums} is: {max_subarray(nums)}" )

nums = [-1, -3, 4, 2]
print(f"Max subsequence for {nums} is: {max_subarray(nums)}" )

nums = [-1, 2, -5, 7]
print(f"Max subsequence for {nums} is: {max_subarray(nums)}" )

nums = [-1, 2, -5, 7, -1, 3]
print(f"Max subsequence for {nums} is: {max_subarray(nums)}" )
