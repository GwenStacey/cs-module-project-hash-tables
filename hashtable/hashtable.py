class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current
        
            current = current.next

        return None

    def insert_at_tail(self, key, value):
        node = HashTableEntry(key, value)

        # if there is no head
        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = node

    def delete(self, key):
        current = self.head

        # if there is nothing to delete
        if current is None:
            return None

        # when deleting head
        if current.key == key:
            self.head = current.next
            return current

        # when deleting something else
        else:
            previous = current
            current = current.next

            while current is not None:
                if current.key == key: # found it!
                    previous.next = current.next  # cut current out!
                    return current # return our deleted node

                else:
                    previous = current
                    current = current.next

            return None # if we got here, nothing was found!

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=8):
        self.capacity = capacity
        self.storage = [None] * self.capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        fnv_prime = 1099511628211
        fnv_hash = 14695981039346656037
        encoded = key.encode("ascii")
        for i in encoded:
            fnv_hash *= fnv_prime
            fnv_hash^i
        return fnv_hash
                
                    


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % len(self.storage)
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hashed_index = self.hash_index(key)
        if self.storage[hashed_index] == None:
            #If the hashtable index is empty, create a LL and insert the 
            #key value pair
            self.storage[hashed_index] = LinkedList()
            self.storage[hashed_index].insert_at_tail(key, value)
        else:
            #Otherwise check it if matches the existing keys
            if self.storage[hashed_index].find(key) is not None:
                self.storage[hashed_index].find(key).value = value
            else:
                #Otherwise just add it to the tail
                self.storage[hashed_index].insert_at_tail(key, value)





    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hashed_index = self.hash_index(key)
        self.storage[hashed_index].delete(key)
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hashed_index = self.hash_index(key)
        if self.storage[hashed_index] == None:
            return None
        else:
            node = self.storage[hashed_index].find(key)
            if node == None:
                return None
            else:
                return node.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_slots = abs(self.capacity - new_capacity)
        self.capacity = new_capacity
        self.storage.append([None]*new_slots)
        for i in self.storage:
            if i != None:
                node = i.head
                next_node = node.next
                while node:
                    self.delete(node.key)
                    self.put(node.key,node.value)
                    node = next_node
                    next_node = node.next
                



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
