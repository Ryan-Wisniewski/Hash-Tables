# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        new_index = self._hash_mod(key)
        #start at front and work back
        head = self.storage[new_index]
        if head is None:
            head = LinkedPair(key, value)
            # print('noneHeadAdding', head)        
        else:
            current_index = head
            # print('ExsistsHeadAdding',current_index)
            while current_index.next is not None:
                current_index = current_index.next
            current_index.next = LinkedPair(key, value)
        self.storage[new_index] = head
        # print('@@@@', LinkedPair)
    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        
        for i in range(0, self.capacity):
            head = self.storage[i]
            print(head, key)
            
            
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        for i in range(0, self.capacity):
            head = self.storage[i]
            if head is None:
                print('this is not the Droid youre l00king for')
                pass
            elif head.key == key:
                value = head.value
                print('$$$HeadIn first value of loop',value)
            else:
                while head.next is not None:
                    head = head.next
                    if key == head.key:
                        value = head.value
                        print('$$$HeadSetAfterLoop',value)
        return value

        # retrieve_hash = self._hash_mod(key) THIS RETURNS INDEX OF THE ARRAY
        # print(retrieve_hash)


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_hashTable = HashTable(self.capacity * 2)
        # print(new_hashTable,self.storage,'@@@@@@@@@@')
        for i in range(0, self.capacity):
            # print(i)
            new_hashTable.storage[i] = self.storage[i]
        self.storage = new_hashTable.storage
        self.capacity = new_hashTable.capacity
        # print(len(ht.storage))
        # print(self.storage)



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    ht.insert("line_4", "Screeee")
    ht.insert("line_5", "SCreeee take2!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht.retrieve("line_4"))
    print(ht.retrieve("line_5"))
    
    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)
    

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht.retrieve("line_4"))
    print(ht.retrieve("line_5"), '\n')

    print(f"\nRemoving: ", ht.remove("line-4"))
    print("Removed?", ht.retrieve("line_4"))
    print("")
    print(ht.__dict__, 'all of itt')