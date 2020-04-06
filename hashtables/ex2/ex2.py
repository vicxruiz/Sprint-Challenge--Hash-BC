#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * (length - 1)

    for ticket in tickets:
        hash_table_insert(ht, str(ticket.source), str(ticket.destination))

    counter = 0
    destination = True
    prev = 'NONE'
    for _ in range(length - 1):
        print('loop ', counter)
        destination = hash_table_retrieve(ht, str(prev))
        route[counter] = destination
        prev = destination
        counter += 1

    return route