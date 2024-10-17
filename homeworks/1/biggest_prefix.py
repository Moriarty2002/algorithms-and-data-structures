
# Find the biggest prefix in a list of words
# usind a dividi et impera algorithm


def check_prefix(word_1: str, word_2: str) -> str:
    
    found_prefix: str = ""  
    
    for i in range(min(len(word_1), len(word_2))):
        if word_1[i] == word_2[i]:
            found_prefix += word_1[i]
        else:
            break
    
    return found_prefix


def find_biggest_common_prefix(words_list):
    
    listLen = len(words_list)
    
    if listLen == 1:
        return words_list[0]

    elif listLen == 2:
        return check_prefix(words_list[0], words_list[1])
    
    else:
        split_index = listLen // 2
        return check_prefix( 
                            find_biggest_common_prefix(words_list[0:split_index]),
                            find_biggest_common_prefix(words_list[split_index:listLen])
                            )


if __name__ == "__main__":
    
    words = ["test", "testa", "tesi", "testuggine", "teso"]
    print(find_biggest_common_prefix(words))
    
    words = ["apple", "ape", "april", "applied"]
    print(find_biggest_common_prefix(words))

    words = ["usain", "usainv", "usainfe", "usaine", "usaine"]
    print(find_biggest_common_prefix(words))

    words = ["test", "testa", "tesi", "testuggine", "amaringo"]
    print(find_biggest_common_prefix(words))




# print(check_prefix("mammt", "mamre"))