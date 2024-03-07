class Node:
    def __init__(self, key, val) -> None:
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class DLL:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.rear == None
    
    def addTohead(self, node):
        if not self.rear:
            self.front = self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        return node
    
    def moveTohead(self, node):
        if self.front == node:
            return
        elif self.rear == node:
            self.rear = self.rear.prev
            self.rear.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.next = self.front
        self.front.prev = node
        self.front = node

    def removefromRear(self):
        page = self.rear
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        return page.key

class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.mp = {}
        self.pageList = DLL()


    def get(self, key):
        if key not in self.mp:
            return "Page Not Found"
        
        page = self.mp[key]
        self.pageList.moveTohead(page)

    def put(self, key, value):
        node = Node(key, value)
        if self.capacity == 0:
            del self.mp[self.pageList.removefromRear()]
            self.capacity += 1
        self.capacity -= 1
        self.pageList.addTohead(node)
        self.mp[key] = node

obj = LRUCache(2)
print(obj)
obj.put(1, 12)
print(obj.pageList)
print(obj.mp)
obj.put(12, 21)
print(obj.pageList)
print(obj.mp)
obj.put(11, 21)
print(obj.pageList)
print(obj.mp)
