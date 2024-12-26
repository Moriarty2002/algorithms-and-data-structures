"""
Si consideri un algoritmo di tipo Divide et Impera D che opera su un array di interi con 1 ≤ n ≤ 1000
elementi. Al primo passo l’algoritmo divide l’array in due parti; successivamente continua a dividere
solo uno dei due sotto-array. Il numero di divisioni da fare e l’insieme dei pivot da usare (ossia i punti
in cui si dovrà suddividere l’array) sono dati in ingresso. Ad ogni operazione di suddivisione fatta da
Alg è associato un costo, che è pari al numero di elementi dell’array (o del sotto-array) da
suddividere. È facile notare che selezioni diverse nell'ordine dei pivot (ossia dove suddividere prima)
possono portare a costi diversi. Ad esempio, si consideri un array di 100 elementi, e siano i possibili
pivot 25, 50 e 75. Ci sono diverse scelte. L’algoritmo D può suddividere prima a 25, poi a 50, poi a
75. Questo porta ad un costo di 100 elementi + 75 elementi + 50 elementi = 225 perché il primo
array era di 100 elementi, il secondo, risultante dalla prima suddivisione, di 75 e l'ultima, risultante
dalla seconda suddivisione, di 50. Un’altra scelta potrebbe essere scegliere come pivot 50, poi a 25,
poi a 75. Questo porterebbe a un costo di 100 + 50 + 50 = 200, che è migliore. Si progetti un algoritmo
per determinare il costo minimo che D impiega per suddividere l’array il numero di volte indicato.
"""

def subarray_length(arr, p):
    # Find the left boundary (closest 1 or start of array)
    left = p
    while left > 0 and arr[left] != 1:
        left -= 1
    
    # Find the right boundary (closest 1 or end of array)
    right = p
    while right < len(arr) - 1 and arr[right] != 1:
        right += 1
    
    # Return the length of the subarray
    return right - left #+ 1

# # Example usage
# arr = [0, 0, 1, 0, 0, 1, 0, 1]
# p = 4
# result = subarray_length(arr, p)
# print(f"The length of the subarray is: {result}")


def find_min_cost(n, pivots: list, found: dict = None, arr: list = None) -> int:
    cost = None
    
    if found is None:
        found = {}
        arr = [0 for _ in range(n)]
        cost = n + 1
        
    if not pivots:
        return 0
    
    pivots_key = '-'.join(str(p) for p in sorted(pivots))
    
    if pivots_key in found:
        return found[pivots_key]
    else:
        found[pivots_key] = float('inf')
    
    for p in pivots:
        
        arr_p = arr[:]
        arr_p[p-1] = 1
        
        cost = subarray_length(arr, p-1) if cost is None else cost
        
        found[pivots_key] = min( 
                                 found[pivots_key],
                                 find_min_cost(n, [x for x in pivots if x != p], found, arr_p) + cost
                                )
    
    return found[pivots_key]

if __name__ == "__main__":
    
    n = 100
    pivots = [25, 75, 100]
    print(f"RES:  { find_min_cost(n, pivots)  } ")
    
    n = 30
    pivots = [2, 20, 25]
    print(f"RES:  { find_min_cost(n, pivots)  } ")
    
    
    n = 10
    pivots = [4, 5, 7, 8]
    print(f"RES:  { find_min_cost(n, pivots)  } ")
    
