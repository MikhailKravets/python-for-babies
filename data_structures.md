# Data Structures

## Stack vs Heap



## Arrays

Array example Python

```python
l = []
```


### Static vs Dynamic

`int` size is 4 bytes.

Dynamic Array is stored in Heap.

```python
l = []
l.append(1)
```

`l.append(1)` has a time complexity of amortized O(1).
`l.pop()` has a time complexity of O(1).
`l.insert(3)` has a time complexity of O(n).
`l.pop(1)` has a time complexity of O(n).

## Hash Map

```python
d = {
    "alice": 25
}
```

`d["key"]` has a time complexity of amortized O(1).

`"alice" in d` has a time complexity O(1).

### Resolve Collisions

* Use linked lists
* Use Open Addressing

## Hash Set

The same Hash Map but without values.

## Linked List

* Single Linked List
* Double Linked List

```python
class LinkedList:

    def __init__(self, val: int, next: 'LinkedList'):
        self.val = val
        self.next = next


root = LinkedList(1)
root.next = LinkedList(2)
root.next.next = LinkedList(3)


def follow(root: LinkedList):
    pointer = root

    while pointer is not None:
        print(pointer)
        pointer = pointer.next


def delete(root: LinkedList, val: int):
    pointer = root
    prev = None

    while pointer:
        if pointer.val == val:
            prev.next = prev.next.next
            break
        prev = pointer
```

* `Get` operation has time complexity O(n).
* `Delete` first element from Linked List has O(1)