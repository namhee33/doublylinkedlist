class Node(object):
	def __init__(self, value=0, prev=None, next=None):
		self.value = value
		self.prev = prev
		self.next = next

class DoublyLinkiedList(object):
	def __init__(self, first=None, last=None):
		self.first = first
		self.last = last

	def traverse_forward(self):
		node = self.first
		while node is not None:
			print node.value,
			node = node.next
		print
		return self

	def traverse_backward(self):
		node = self.last
		while node is not None:
			print node.value, 
			node = node.prev
		print
		return self

	def insertAfter(self, node, newNode):
		newNode.next = node.next
		newNode.prev = node
		if node.next is None:
			self.last = newNode
		else:
			node.next.prev = newNode
		node.next = newNode
		
	def insertBefore(self, node, newNode):
		newNode.prev = node.prev
		newNode.next = node
		if node.prev is None:
			self.first = newNode
			
		else:
			node.prev.next = newNode
		node.prev = newNode
		return self

	def insertBeginning(self, newNode):
		if self.first is None:
			self.first = newNode
			print 'set first: (beginning)', newNode.value
			self.last = newNode
			newNode.prev = None
			newNode.next = None
		else:
			self.insertBefore(first, newNode)
		return self

	def insertEnd(self, newNode):
		if self.last is None:
			self.insertBeginning(newNode)
		else:
			self.insertAfter(self.last, newNode)

		return self

	def insertAfter_with_value(self, value, newNode):
		node = self.find(value)
		if node is not None:
			self.insertAfter(node, newNode)

	def insertBefore_with_value(self, value, newNode):
		node = self.find(value)
		if node is not None:
			self.insertBefore(node, newNode)

	def find(self, value):
		node = self.first
		while node is not None:
			if node.value == value:
				return node
			node = node.next
		print 'can\'t find it!'
		return 

	def delete_node(self, node):
		if node.prev is None:
			self.first = node.next
		else:
			node.prev.next = node.next
		if node.next is None:
			self.last = node.prev
		else:
			node.next.prev = node.prev

	def remove(self, value):
		node = self.find(value)
		if node is not None:
			self.delete_node(node)

list1 = DoublyLinkiedList()
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
list1.insertEnd(node1).insertEnd(node2).insertEnd(node3)
list1.traverse_forward()
list1.remove(10)
list1.traverse_forward()
node4 = Node(25)
list1.insertAfter_with_value(20, node4)
list1.traverse_forward()
node5 = Node(35)
list1.insertBefore_with_value(30, node5)
list1.traverse_forward()



