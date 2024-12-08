import sys

def find_optimal(V: int, coins: list, memoized_optimal: list = None) -> int:
        
    if memoized_optimal is None:            # Create memoization array in first call
        memoized_optimal = [None for _ in range((V + 1))]
    
    # Base Case 
    if len(coins) == 0 or V == 0:           # base case
        return 0

    if V < 0:                               # invalid option
        return sys.maxsize  
    
    if memoized_optimal[V] is not None:     # check if already memoized
        return memoized_optimal[V]

    memoized_optimal[V] = sys.maxsize
    
    for coin in coins:
                
        memoized_optimal[V] = min (
            find_optimal(V - coin, coins, memoized_optimal) + 1,
            find_optimal(V, coins, memoized_optimal),
            memoized_optimal[V]
        )
    
    return memoized_optimal[V]


def find_suboptimal(V: int, coins: list, memoized_optimal: list = None) -> int:
    
    
    is_first_call = False
    
    if memoized_optimal is None:            # Create memoization array in first call
        memoized_optimal = [None for _ in range((V + 1))]
        memoized_optimal_2 = [None for _ in range((V + 1))]
        is_first_call = False
    
    # Base Case 
    if len(coins) == 0 or V == 0:           # base case
        return 0

    if V < 0:                               # invalid option
        return sys.maxsize  
    
    if memoized_optimal[V] is not None:     # check if already memoized
        return memoized_optimal[V]

    memoized_optimal[V] = sys.maxsize
    
    for coin in coins:
        
        if V - coin >= 0:
        
            memoized_optimal[V] = min (
                find_suboptimal(V - coin, coins, memoized_optimal) + 1,
                find_suboptimal(V, coins, memoized_optimal),
                memoized_optimal[V]
            )

        # TODO: Gestire caso valore esatto non trovato    
    
    if memoized_optimal[V] == sys.maxsize:
        memoized_optimal[V] = find_suboptimal(0, coins, memoized_optimal) + 1
    
    return memoized_optimal[V]


if __name__ == "__main__":
    
    V = 10
    coins = [1, 5]
    print(f"\nBudget: {V}, Coins: {coins} \nSolution (min number of coins): {find_suboptimal(V, coins)}")
    
    
    V = 7
    coins = [1, 3, 4, 5]
    print(f"\nBudget: {V}, Coins: {coins} \nSolution (min number of coins): {find_suboptimal(V, coins)}")
    
    V = 59
    coins = [2, 7, 15]
    print(f"\nBudget: {V}, Coins: {coins} \nSolution (min number of coins): {find_suboptimal(V, coins)}")
    
    V = 99
    coins = [10, 20, 30, 12]
    print(f"\nBudget: {V}, Coins: {coins} \nSolution (min number of coins): {find_suboptimal(V, coins)}")
    
    V = 3
    coins = [7, 15]
    print(f"\nBudget: {V}, Coins: {coins} \nSolution (min number of coins): {find_suboptimal(V, coins)}")
    
    V = 0
    coins = [2, 7, 15]
    print(f"\nBudget: {V}, Coins: {coins} \nSolution (min number of coins): {find_suboptimal(V, coins)}")
    
    V = 13
    coins = []
    print(f"\nBudget: {V}, Coins: {coins} \nSolution (min number of coins): {find_suboptimal(V, coins)}")
    
    