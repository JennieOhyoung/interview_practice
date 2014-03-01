
"""
Implement a function that takes (circle of people, steps to skip) and returns the last person remaining. aka the josephus problem
"""

class Queue(object):
    def __init__(self):
        self.items = []
    def __str__(self):
        return str(self.items)
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []

players = list('abcdefghijklmnopqrstuvwxyz')
players2 = range(0,100)

def make_circle(players):
    circle = Queue()
    for i in players:
        circle.enqueue(i)
    return circle

def josephus(players, skip):
    circle = make_circle(players)
    while circle.size()>1:
        for i in range(skip):
            circle.enqueue(circle.dequeue())
        circle.dequeue()
    return circle.dequeue()


print josephus(players, 5)
print josephus(players2, 1)











