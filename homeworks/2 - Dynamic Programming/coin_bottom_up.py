def min_num_coins(V, coins):
    # Inizializziamo un array dp di dimensione V+1 con un valore molto grande (infinito)
    dp = [float('inf')] * (V + 1)
    
    # Per pagare 0 centesimi, servono 0 monete
    dp[0] = 0

    # Iteriamo sugli importi da 1 fino a V
    for i in range(1, V + 1):
        # Per ogni moneta disponibile
        for coin in coins:
            if i - coin >= 0:  # Se possiamo usare la moneta
                dp[i] = min(dp[i], dp[i - coin] + 1)  # Aggiorniamo il numero minimo di monete

    # Se dp[V] è ancora infinito, significa che non è possibile pagare esattamente V centesimi
    # con le monete fornite. Restituiamo -1 in quel caso, altrimenti restituiamo dp[V].
    return dp[V] if dp[V] != float('inf') else -1

# Esempio di utilizzo
V = 10
coins = [1, 5]

# Calcolo del numero minimo di monete
result = min_num_coins(V, coins)
print(f"Il numero minimo di monete per pagare {V} centesimi è: {result}")
