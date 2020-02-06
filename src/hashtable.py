# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # def __str__(self):
    #     return f'key: {self.key}, value: {self.value}'

    def __repr__(self):
        return f'(key: {self.key}, value: {self.value}, next: {self.next})'

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def __repr__(self):
        return f'storage: {self.storage}'

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

        new_item = LinkedPair(key, value)
        address = self._hash_mod(key)
        
        curr_node = self.storage[address]
        prev_node = None

        while curr_node is not None and curr_node.key is not key:
            prev_node = curr_node
            curr_node = prev_node.next

        if curr_node is not None:
            curr_node.value = value

        else:
            new_item.next = self.storage[address]
            self.storage[address] = new_item

        print(self.storage)

        # if curr_node is None: 
        #     new_item.next = self.storage[address]
        #     print(f'self.storage: {self.storage[ad]}')
        #     print(f'curr_node was none: {new_item}')
        #     self.storage[address] = new_item
        # else:
        #     curr_node.value = value
        #     # curr_node = self.storage[address]
        #     # prev_node = None
        #     print(f'og curr_node: {curr_node}')

        #     # if curr_node.key is key:
        #     #     curr_node = new_item
        #     #     print("match found")

        #     while curr_node is not None and curr_node.key is not key:
        #         print(f'while loop: curr_node: {curr_node}')

        #         prev_node = curr_node
        #         print(f'while loop: prev_node: {prev_node}')
        #         curr_node = prev_node.next
        #         print(f'while loop: curr_node: {curr_node}')

        #         # if curr_node.key is key:
        #         #     prev_node = new_item
        #         #     print("match found")
        #         #     break
        #         # else: 
        #         #     prev_node = curr_node
        #         #     curr_node = curr_node.next

        #     print(f'ult curr_node: {curr_node}')
        #     print(f'ult prev_node: {prev_node}')
        #     # prev_node.next = new_item 

        # # print(f'inserted: ({new_item.key}, {new_item.value})')
        # print(self.storage)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
      
        address = self._hash_mod(key)

        curr_node = self.storage[address]
        prev_node = None

        while curr_node is not None and curr_node.key is not key:
            prev_node = curr_node
            curr_node = prev_node.next
        
        if curr_node is None:
            print(f'Cannot find key')
        else:
            if prev_node is None:
                self.storage[address] = curr_node.next
            else:
                prev_node.next = curr_node.next

        print(self.storage)

        # if self.storage[address] is None:
        #     print('Nothing here...')
        # else: 
        #     curr_node = self.storage[address]
        #     if curr_node.key is key:
        #         self.storage[address] = None
        #     else:
        #         curr_node = self.storage[address]
        #         prev_node = None
        #         while curr_node.key is not key:
        #             prev_node = curr_node
        #             curr_node = curr_node.next
                
        #         prev_node.next = None
            

        # # print (f'removed: {self.storage[address]}')
        # print (self.storage)
        
        # self.storage.remove(self.storage[address])

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        address = self._hash_mod(key)

        curr_node = self.storage[address]

        while curr_node is not None: 
            if curr_node.key is key:
                print(curr_node.value)
                return curr_node.value
            curr_node = curr_node.next

        # if self.storage[address].key is key:
        #     print(self.storage[address])
        #     return self.storage[address].value
        # else:
        #     curr_node = self.storage[address]
        #     # prev_node = None

        #     while curr_node.key is not key:
        #         # prev_node = curr_node
        #         curr_node = curr_node.next

        #     print(f'found: {curr_node}')
        
        # # print(f'retrieved: {self.storage[address]}')
        # return self.storage[address].value
        # # return self.storage[address]



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        prev_storage = self.storage

        self.capacity *= 2

        self.storage = [None] * self.capacity

        curr_node = None

        for slot in prev_storage:
            curr_node = slot
            while curr_node is not None:
                self.insert(curr_node.key, curr_node.value)
                curr_node = curr_node.next

        print(self.storage)

        # new_storage = [None] * self.capacity * 2

        # for slot in self.storage:
        #     new_storage.append(slot)

        # print(new_storage)

hashbrown = HashTable(5)
hashbrown.insert(3, 10)
# hashbrown.insert(3, 12)
hashbrown.insert(8, 15)
hashbrown.insert(8, 20)
hashbrown.insert(13, 20)
# hashbrown.insert(8, 12)
# hashbrown.insert(13, 3)
# hashbrown.insert(8, 20)
# hashbrown.insert(18, 90)
# hashbrown.retrieve(3)
hashbrown.retrieve(3)
hashbrown.remove(8)
# hashbrown.resize()
hashbrown.resize()


# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")