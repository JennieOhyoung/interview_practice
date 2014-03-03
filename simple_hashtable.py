"""
Implement a simple hashtable
Analysis: if no collision occurs, runtime = O(1).
High lambda increases collision which leads to more comparison to find empty slot. 
"""

class Hashtable(object):
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key, size):
        return key%size

    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data #replace

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def get(self,key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key,data)



H = Hashtable()
H[54]="a"
H[26]="b"
H[93]="c"
H[17]="d"
H[77]="e"
H[31]="f"
H[44]="g"
H[55]="h"
H[20]="i"
print H.slots
print H[20]
print H.data
