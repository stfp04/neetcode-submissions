type LinkedList struct {
	value int
	length int
	next *LinkedList
}

func NewLinkedList() *LinkedList {
	var head *LinkedList = &LinkedList{}
	return head
}

func (ll *LinkedList) Get(index int) int {
	var curr *LinkedList= ll.next
	var i int = 0
	for curr != nil && i<index {
		curr = curr.next
		i++
	}
	if curr != nil {
		return curr.value
	} else {
		return -1
	}
}

func (ll *LinkedList) InsertHead(val int) {
	var node *LinkedList = &LinkedList{value: val, next: ll.next}
	ll.next = node
	ll.length++
}

func (ll *LinkedList) InsertTail(val int) {
	curr := ll
	for curr.next != nil {
		curr = curr.next
	}
	var node *LinkedList = &LinkedList{value: val, next: nil}
	curr.next = node
	ll.length++
}

func (ll *LinkedList) Remove(index int) bool {
	var parent *LinkedList = nil
	curr := ll.next
	
	var i int = 0
	for curr != nil && i < index {
		parent = curr
		curr = curr.next
		i++
	}
	if curr == nil {
		return false
	}
	if parent == nil {
		ll.next = curr.next
	} else {
		parent.next = curr.next
	}
	ll.length--
	return true
}

func (ll *LinkedList) GetValues() []int {
	var res []int = make([]int,0,ll.length)
	
	curr := ll.next
	for curr != nil {
		res = append(res, curr.value)
		curr = curr.next
	}
	return res
}
