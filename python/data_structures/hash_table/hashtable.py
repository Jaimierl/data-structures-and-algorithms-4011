from operator import contains
# Questions -
# Setting and Collisions
# Traversing through contains
# Test 4 - your attribute means method and was not built in. Property would be node.property.
# How do we overwrite keys/traverse the linked list at an index?

# LinkedList/Node to create insert and traverse.
# The traverse we just did in class, either rewrite it or write it out in your new function to do what you need to do.
# You should rewrite your traversal so it is custom every time, you can't use it like you built it in in general

# The hashtable could be a list of lists or something too. The collision handling is part of the hashtable, not the linkedlist
# You would want to build your new function in the hash table because it would be a function of the hash table.

# The hashmap is a list
# The index will have the reference to the linked list
# If current index is none, create a new linked list and make the linked list the item at that linked list. Then its traversing the list. To call it, hash_map_list[0] will automatically put you into the linkedlist head if there is a linkedlist there.

# Making a list of objects, specifying a certain number and putting objects into weird indicies.

class Hashtable:
    """
    Several functions that can be used for a Hashtable implementation. The Key refers to the string that you would like to add to the hash table.
    """

    #Sanitize the input to make sure that you have a string. ie. turn numbers into strings.
    # We need to write/import linked list and node for this.
    # If you are adding to an index, does something exist at the index or not?
    # If there is nothing at the index? Need to create a new linked list at that index
    # Assigning something to a list like putting a number into a list. list[index] = LinkedList()
    # If there is a linked list there

    def __init__(self, size = 3):
        # Change the size back to 1024 when you're done.
        # We are taking the list and filling the values with None in every index to begin with. We are giving the list the length of 10224 to begin with.
        self.size = size
        self._buckets = size * [None]

    def hash(self,key):
        """Argument: key - which is the input string
        Returns: Index in the collection for that key somewhere between 0 and one less that the size of the list.
        Convert each item in the given array using the ord() method.
        Total the ord() method values amd multiply by a larger prime number to induce more randomness into the conversion
        Take the modulus of the total as compared to the length of the hash table
        Return the number of the index"""

        sum = 0

        for character in key:
            sum += ord(character)

        primed = sum*23

        index = primed % self.size

        return index

    def set(self,key,value):
        """Adds an item to the hash table"""
        """ Arguments: key, value
        Returns: nothing
        This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
        """
        if key is None:
            return

        key = str(key)
        #print(key)

        index = self.hash(key)
        #print(index)

        linked = LinkedList()


        linked.insert([key,value])
        self._buckets[index] = linked.head
            # The insert function handles making the new value the head if a value is there and adding a value if nothing is there.

        # This makes no sense - if you are storing the keys why would there be collisions? Could multiple keys and multiple values exist at the same index/ stored as the linkedlist value?

    def get(self,key):
        """Returns the head of anything at this value in the linked list. """
        """Arguments: key
        Returns: Value associated with that key in the table"""
        index = self.hash(key)
        # You still need to check whether the index is none
        # Current = hashtable[index].head
        # How it has the key/value as the value and the next. You can now check the key against what you are looking for.
        # If there is no next, go back to the head and insert the new key/value pair into the head of the linked list.
        # You would need to go back to Current = hashtable[index].head to insert the new node there at the head.

        keys_value = self._buckets[index].value[1]
        # The second value is there because otherwise you would just return the hashtable/linked list object
        return keys_value

    def contains(self,key):
        """Argument: Key
        Objective Return Statement: Boolean, indicating if anything is in the bucket/ key exists in the hash table already.
        Actual Return Statement: Since I am not sure how to unhash something to make sure that specific thing is already used as a key, we are going to return True if there is already a value at this index. Ie. if two keys lead to the same hash value and one of them has a value in the table, this will still come back as True."""
        # Is there anything at this index? Is it the key sent in? If not is the next thing that value?
        # This also would mean traversing the linkedlist if you are saving things as key/value pairs
        contained = False
        index = self.hash(key)
        if self._buckets[index].value[1]:
            pass

        for index in self._buckets:
            if self._buckets[index] is not None:
                pass

    def keys(self):
        """Argument: key
        returns: Collection of keys at all indices, aka the whole hash table.Return all of the keys where the value is not none. It is an index before any value is assigned, a key when a value is assigned."""
        list_of_keys = []

        for index in self._buckets:
            print(index)
            if index is not None:
                self._buckets[index].traverse
            #     # How would we traverse this?
            #     print(index)
                # list_of_keys.append(self._buckets[index].value[0])
                # How would we append something that is being returned as printed (from the traverse function in the linked list)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList():
    """
    This is the LinkedList Class
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    # This function currently makes a new node by calling the class node and passing in a value. Then it reassigns the new Node to the head of the Linked List.

    def traverse(self):
        # From class - want to use to test the insert function
        current = self.head
        while current:
            # This is saying while current is not none
            print(current.value)
            current = current.next

    def includes(self, value):
        # This function should indicate whether that value exists as a Node’s value somewhere within the list.
        # Should RETURN a Boolean
        current = self.head

        while current:
            if value == current.value:
                # Here we needed to tell the function to look at the VALUE of the item or node we are on.
                return True
            # End the loop if the answer is what you were looking for
            else:
                current = current.next
                # Go to the next item in the list if the item you were on was not the answer you are looking for
        else:
            return False
        # Apparently else works with while for an alternative to if the condition in the while loop is not met and the loop exhausts its paths.
        # This should return the other side of the boolean once current runs out of items in the list.

    def __str__(self):
        # This function should RETURN a string representing all the values in the Linked List
        # Self counts as no arguments because it is a method on its-SELF
        # This is a string method  - like the dunder str and dunder repr from before (__str__)
        # This is the client facing string that shows if you just PRINT the class, no need to call with the dunder stuff.
        # The __repr__ is the dev facing piece. This is called with the repr dunder tags
        returned_string = ""
        current = self.head
        while current:
            returned_string += "{ " + current.value + " } -> "
            current = current.next

        returned_string += "None"
        # None is the Null of python - you can update the test to match.
        # returned_string.strip('\'')
        return returned_string






