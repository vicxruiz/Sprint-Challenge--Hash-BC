#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(length):
            hash_table_insert(ht, weights[i], i)
    answer = None
    for i in range(length):
        if (hash_table_retrieve(ht, limit - weights[i]) and hash_table_retrieve(ht, limit - weights[i]) != i):
            hash_index = hash_table_retrieve(ht, limit - weights[i])
            if hash_index > i:
                answer = (hash_index, i)
            else:
                answer = (i, hash_index)
    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")