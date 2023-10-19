from collections import deque
import copy
import sys
import heapq


tree = {}
printList = []
n = int(sys.stdin.readline())
for _ in range(n):
    root,left,right = map(str,sys.stdin.readline().strip().split())
    tree[root] = [left,right]

def preorder(node,tree):
    if node == '.':
        return

    printList.append(node)
    preorder(tree[node][0],tree)
    preorder(tree[node][1],tree)

preorder('A',tree)
print(''.join(map(str,printList)))
printList.clear()

def inorder(node, tree):
    if node == '.':
        return
    inorder(tree[node][0],tree)
    printList.append(node)
    inorder(tree[node][1],tree)

inorder('A',tree)
print(''.join(map(str,printList)))
printList.clear()

def postorder(node,tree):
    if node == '.':
        return
    postorder(tree[node][0],tree)
    postorder(tree[node][1],tree)
    printList.append(node)

postorder('A',tree)
print(''.join(map(str,printList)))