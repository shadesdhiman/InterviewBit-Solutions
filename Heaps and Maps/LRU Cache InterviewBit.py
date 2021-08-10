class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
H = Node(1)
start = H
T = Node(-1)
H.next = T
T.prev = H


class LRUCache(Node):
    dic = dict()
    arr = []
    

    
    def __init__(self, capacity):
        self.capacity = capacity
        self. dic = {}
        self.arr = []
        self.head = None
    
    
    
        
        
    
      
        # @return an integer
    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            (node.prev).next = node.next
            (node.next).prev = node.prev
            node.prev = H
            node.next = H.next
            H.next = node
            (node.next).prev = node
            
            return self.dic[key].data
        else:
            return -1
            


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value): 
        if key in self.dic:
            
            node = self.dic[key]
            node.data = value
            (node.prev).next = node.next
            (node.next).prev = node.prev
            node.prev = H
            node.next = H.next
            H.next = node
            (node.next).prev = node
           
            
            
            
        else:
            node = Node(value)
            self.dic[key] = node
            node.prev = H
            node.next = H.next
            H.next = node
            (node.next).prev = node
            
            
            
        if len(self.dic)> self.capacity:
            temp = T.prev
        
            (temp.prev).next = T
            T.prev = temp.prev
            for key, value in self.dic.items():
                  if value == temp:
                    del self.dic[key]
                    break
            


obj = LRUCache(capacity = 1)

print(obj.set(2,1))
print(obj.get(2))   
  
print(obj.set(3,2))

print(obj.get(2))
print(obj.get(3))