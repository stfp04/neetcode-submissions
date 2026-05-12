
type ListNode struct {
	val int
	next *ListNode
}

func NewListNode(val int, next *ListNode) *ListNode {
	return &ListNode{
		val: val,
		next: next,
	}
}


type LinkedList struct {
	head *ListNode
	tail *ListNode
	length int
}


func NewLinkedList() *LinkedList {
	head := NewListNode(-1, nil)
	tail := head

	return &LinkedList{
		head: head,
		tail: tail,
		length: 0,
	}
}

func (ll *LinkedList) Get(index int) int {
	curr := ll.head.next
	i := 0
	for curr != nil{
		if i == index{
			return curr.val
		}
		curr = curr.next
		i++
	}
	return -1
}

func (ll *LinkedList) InsertHead(val int) {
	newNode := NewListNode(val,ll.head.next)
	ll.head.next = newNode
	if newNode.next == nil {
		ll.tail = newNode
	}
}

func (ll *LinkedList) InsertTail(val int) {
	newNode := NewListNode(val, nil)
	ll.tail.next = newNode
	ll.tail = ll.tail.next
}

func (ll *LinkedList) Remove(index int) bool {
	curr := ll.head
	i := 0
	// ok if im removing a node i need the previous node to point to the next.next node
	//also need to be aware of the fact that next.next could be nil so need a check for that

	for i < index && curr != nil {
		i++
		curr = curr.next
	}

	if curr != nil && curr.next != nil {
		if curr.next == ll.tail{
			ll.tail = curr
		}
		curr.next = curr.next.next
		return true
	}

	

	return false

}

func (ll *LinkedList) GetValues() []int {
	curr := ll.head.next 
	var res []int

	for curr != nil{
		res = append(res,curr.val)
		curr = curr.next
	}

	return res
}
