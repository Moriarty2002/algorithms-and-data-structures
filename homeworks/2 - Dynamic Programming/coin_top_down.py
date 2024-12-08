# TOP DOWN:     recursion + memoization

def min_num_coins_top_down(V, coins, memo):
    # Se V è 0, non servono monete
    if V == 0:
        return 0
    # Se l'importo è negativo, non esiste una soluzione
    if V < 0:
        return float('inf')  # Simile a un valore infinito, impossibile
    
    # Se abbiamo già calcolato la soluzione per V, la restituiamo
    if memo[V] != -1:
        return memo[V]
    
    # Variabile per tenere traccia del minimo numero di monete
    min_coins = float('inf')
    
    # Proviamo ogni moneta
    for coin in coins:
        res = min_num_coins_top_down(V - coin, coins, memo)
        if res != float('inf'):
            min_coins = min(min_coins, res + 1)
    
    # Salviamo la soluzione trovata in memo e la restituiamo
    memo[V] = min_coins
    return memo[V]

def min_num_coins(V, coins):
    # Inizializziamo una tabella di memoization con -1 (valore non calcolato)
    memo = [-1] * (V + 1)
    result = min_num_coins_top_down(V, coins, memo)
    return result if result != float('inf') else -1

# Esempio di utilizzo
V = 10
coins = [1, 5]

# Calcolo del numero minimo di monete con approccio Top-Down
result = min_num_coins(V, coins)
print(f"Il numero minimo di monete per pagare {V} centesimi è: {result}")
