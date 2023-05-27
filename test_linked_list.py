from linked_list import LinkedList


def test_linked_list():
    ll = LinkedList()
    assert ll.head == None


def test_linked_list_insert():
    ll = LinkedList()
    assert ll.head == None
    ll.insert(1)
    assert ll.head.val == 1
    assert ll.head.next == None


def test_linked_list_insert_b():
    ll = LinkedList([2, 1])
    assert ll.head.val == 1
    assert ll.head.next.val == 2
    ll.insert(0)
    assert ll.head.val == 0
    assert ll.head.next.val == 1
    assert ll.head.next.next.val == 2
    assert ll.head.next.next.next == None
