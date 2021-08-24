# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:37:10 2021

@author: Dhiman
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def insert(root,data):
    if root == None:
        return Node(data)
    else:
        if root.data < data:
            root.right =  insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def postorder(root):
    if root:
        inorder(root.left)
        
        inorder(root.right)
        print(root.data)

def search(root, val):
    
    if root:
        if root.data == val:
            print("\nExists !")
        elif root.data < val:
            search(root.right, val)
        elif root. data> val:
            search(root.left, val)
    else:
        print("\nNot Exists!")

def delete(root, val):
    if root:
        if root.data == val:
            if root.left is None and root.right is None:
                return None
            #for only one child
            if root.left is None:
                temp  = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp
            
            
            #if the node have both the childs
            leftibhai = root.left
            leftibhaiprev = root
            
            while(leftibhai.right!= None):
                leftibhaiprev = leftibhai
                leftibhai = leftibhai.right
            if root !=  leftibhaiprev: 
                leftibhaiprev. right = leftibhai.left
            else:
                leftibhaiprev. left = leftibhai.left
            """
                    4
                
                0       6
                
            -1    2  5
            
                1            
            """
       
            
            root.data= leftibhai.data
            return root
                
    
            
        elif root.data < val:
            root. right = delete(root.right, val)
            return root
        elif root. data> val:
            root.left = delete(root.left, val)
            return root
    else:
        return root
    
    
        
    


root = Node(5)
root = insert(root, 3)
root = insert(root, 45)
root = insert(root, 4)
root = insert(root, 34)
root = insert(root, 427)
root = delete(root, 34)
inorder(root)
print(" ")
postorder(root)
    
        
        
    