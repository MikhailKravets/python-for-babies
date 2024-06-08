from ctypes import pointer


class LinkNode:

    def __init__(self, val: int):
        self.val = val
        self.next: None | LinkNode = None

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


def pass_through_list(head: LinkNode):
    pointer = head

    while pointer:  # while pointer is not None:
        print(pointer.val)
        pointer = pointer.next


def remove_node(head: LinkNode, node_index: int) -> LinkNode:
    if node_index == 0:
        return head.next

    i = 0
    pointer = head
    while pointer.next and i < node_index - 1:
        pointer = pointer.next
        i += 1

    if pointer.next is None:
        return head

    pointer.next = pointer.next.next

    return head


def reverse_list(head: None | LinkNode) -> LinkNode:
    if not head:
        return None

    stack = []

    pointer = head
    while pointer:
        stack.append(pointer)
        pointer = pointer.next

    new_head = stack.pop()
    pointer = new_head
    while stack:
        node = stack.pop()
        pointer.next = node
        pointer = pointer.next
    pointer.next = None
    return None


def reverse_list_recursive(head: None | LinkNode) -> LinkNode:
    if not head:
        return None

    nh = None

    # Depth-First Search
    def dfs(head: None | LinkNode):
        if not head.next:
            nonlocal nh
            nh = head
            return head

        pointer = dfs(head.next)
        pointer.next = head
        return head

    dfs(head)

    head.next = None
    return nh


# 1 -> 2 -> 3 -> 4 -> 5 -> None
# 5 -> 4 -> 3 -> 2 -> 1 -> None
if __name__ == "__main__":
    root = LinkNode(1)
    root.next = LinkNode(2)
    root.next.next = LinkNode(3)
    root.next.next.next = LinkNode(4)
    root.next.next.next.next = LinkNode(5)

    # pass_through_list(root)
    # print(remove_node(root, 3))

    print(reverse_list_recursive(root))