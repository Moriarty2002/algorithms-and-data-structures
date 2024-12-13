# Find longest subsequence

def max_subarray(nums, n: int = None, memoized_optimal: list = None, current_max: dict = None):
    is_first_call = False
    
    if n is None: # First call init
        n = len(nums) - 1 
        memoized_optimal = [None for _ in range(n+1)]     
        current_max = {'position': 0, 'value': nums[0]}
        is_first_call = True

    
    if not n: # base case with subsequence of length n
        memoized_optimal[0] = nums[0]
        return nums[0]
    
    if memoized_optimal[n] is not None:
        return memoized_optimal[n]
    
    # Recursivamente trova la somma massima che termina in n
    memoized_optimal[n] = max(nums[n], nums[n] + max_subarray(nums, n - 1, memoized_optimal, current_max))
    
    if memoized_optimal[n] > current_max["value"]:
        current_max["value"] = memoized_optimal[n]
        current_max["position"] = n
    
    if is_first_call:
        return current_max["value"]
    
    return memoized_optimal[n]
    

# Esempio di utilizzo
nums = [4, -1, 2, 1, -5, 4]
print("La somma massima del sottoarray è:", max_subarray(nums))

# Esempio di utilizzo
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("La somma massima del sottoarray è:", max_subarray(nums))


# Esempio di utilizzo
nums = [-1, -3, 4, 2]
print("La somma massima del sottoarray è:", max_subarray(nums))

# Esempio di utilizzo
nums = [-1, 2, -5, 7]
print("La somma massima del sottoarray è:", max_subarray(nums))

# Esempio di utilizzo
nums = [-1, 2, -5, 7, -1, 3]
print("La somma massima del sottoarray è:", max_subarray(nums))