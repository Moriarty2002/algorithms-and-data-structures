# find biggest element in an unimodal array

def search_max(list, start_index: int, len: int) -> int:
    i = (start_index + len) // 2
    
    if start_index == (len-1): # single element case
        return list[i]
    
    if (i==0 or list[i-1]) < list[i] and list[i] > (i == (len-1) or list[i+1]): # found max element
        return list[i]
    
    elif list[i-1] > list[i]: # search left
        return search_max(list, start_index, i-1)
    
    elif list[i+1] > list[i]: # search right
        return search_max(list, i+1, len)


if __name__ == "__main__":
    unimodal_array = [1, 2, 3, 4, 5, 4, 3, 2]
    print(f"Found: {search_max(unimodal_array, 0, len(unimodal_array))}")
    
    unimodal_array = [1, 2, 3, 4, 7]
    print(f"Found: {search_max(unimodal_array, 0, len(unimodal_array))}")
    
    unimodal_array = [1, 2, 8, 10, 8]
    print(f"Found: {search_max(unimodal_array, 0, len(unimodal_array))}")
    
    unimodal_array = [1]
    print(f"Found: {search_max(unimodal_array, 0, len(unimodal_array))}")