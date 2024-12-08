# Dato un certo importo da pagare di V centesimi ed una lista di n monete coin[n] che
# possiamo usare (per esempio n = 3 monete, quelle da 1 centesimo (coin[0] = 1), da 5
# centesimi (coin[1] = 5), da 10 centesimi (coin[2] = 10)), si scriva un algoritmo per
# determinare il numero minimo di monte che dobbiamo usare per arrivare all’importo esatto
# V o al più piccolo importo maggiore di V. Si assuma di avere un numero illimitato di monete
# di tutti i tipi. 
# es. V = 10, n = 2, coin[0] = 1, coin[1] = 5. In tal caso si possono usare:
# - 10 monete da 1 centesimo (10 x coin[0]). Totale monete usare: 10
# - 1 moneta da 5 e 5 monete da 1 (1 x coin[1] + 5 x coin[0]). Totale monete usate: 6
# - 2 monete da 5 (2 x coin[1]). Totale monete usate: 2. La soluzione ottima è questa. 


import sys

def find_min_coin(V: int, coins: list, memoized_optimal: list = None) -> int:
    
    if memoized_optimal is None:            # Create memoization array in first call
        memoized_optimal = [None for _ in range((V + 1))]
    
    # Base Case 
    if len(coins) == 0 or V == 0:           # base case
        return 0
    
    if memoized_optimal[V] is not None:     # check if already memoized
        return memoized_optimal[V]

    memoized_optimal[V] = sys.maxsize
    
    for coin in coins:
        
        if V - coin >= 0:
        
            memoized_optimal[V] = min (
                find_min_coin(V - coin, coins, memoized_optimal) + 1,
                find_min_coin(V, coins, memoized_optimal),
                memoized_optimal[V]
            )
    
    if memoized_optimal[V] == sys.maxsize:
        memoized_optimal[V] = find_min_coin(0, coins, memoized_optimal) + 1
    
    return memoized_optimal[V]


if __name__ == "__main__":
    
    V = 10
    coins = [1, 5]
    print(f"\nTarget: {V}, Coins: {coins} \nSolution (min number of coins): {find_min_coin(V, coins)}")
    
    V = 7
    coins = [1, 3, 4, 5]
    print(f"\nTarget: {V}, Coins: {coins} \nSolution (min number of coins): {find_min_coin(V, coins)}")
    
    V = 59
    coins = [2, 7, 15]
    print(f"\nTarget: {V}, Coins: {coins} \nSolution (min number of coins): {find_min_coin(V, coins)}")
    
    V = 99
    coins = [10, 20, 30, 12]
    print(f"\nTarget: {V}, Coins: {coins} \nSolution (min number of coins): {find_min_coin(V, coins)}")
    
    V = 3
    coins = [7, 15]
    print(f"\nTarget: {V}, Coins: {coins} \nSolution (min number of coins): {find_min_coin(V, coins)}")
    
    V = 0
    coins = [2, 7, 15]
    print(f"\nTarget: {V}, Coins: {coins} \nSolution (min number of coins): {find_min_coin(V, coins)}")
    
    V = 13
    coins = []
    print(f"\nTarget: {V}, Coins: {coins} \nSolution (min number of coins): {find_min_coin(V, coins)}")
    
    