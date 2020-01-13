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
        self.count = 0
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
        if self.count == self.capacity:
            print('attempting to resize')
            self.resize()
            print('resize success. Capacity now: ', self.capacity)
        #loop through hashtable
        for i in range(self.capacity):
            if self.storage[i] is None:
                #set key to new instance of LinkedPair
                new_key = LinkedPair(key, value)
                print('1Check',new_key)
                #hash the key
                new_hash = self._hash(new_key)
                print('2Check',new_hash)
                check = self._hash_mod(key)
                print('grabfromhashcheck', self.storage[check])
                #save the key
                self.storage[i] = new_hash
                print('lastAllCheck',new_hash, self.storage)
            else:
                #handle the hashes beging the same here!!
                print('handle the reapeat hash', self.storage)
        self.count += 1
        # print(self.count,'CHECKHERHEHEEHRE')
         
        # new_hash = self._hash(LinkedPair(key, value))
        # print(new_hash)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        pass
        # retrieve_hash = self._hash_mod(key)
        # print(retrieve_hash)


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        # print(self.capacity)
        new_storage = [None] * self.capacity
        # print(new_storage,self.storage,'@@@@@@@@@@')
        for i in range(self.count):
            print(i)
            new_storage[i] = self.storage[i]
        self.storage = new_storage
        print(self.storage)



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
