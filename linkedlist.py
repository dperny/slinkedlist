from node import Node

class LinkedList:
	"""A Python3 class for linked lists

	full range of operations supported
	"""

	def __init__(self,value = None):
		self._headNode = Node(value,None)
		self._currentNode = self._topNode
		self._tailNode = self._tailNode
		self._size = 1

	def head(self,value = None):
		if(value = None):
			return self._currentNode.head()
		else:
			self._currentNode.setHead(value)

	def tail(self):
		self._currentNode = self.currentNode.tail()

	def top(self):
		self._currentNode = self._headNode

	def bottom(self):
		self._currentNode = self._tailNode

	def frontadd(self,value):
		if(self._headNode.head() == None):
			self._headNode = Node(value,None)
		else:
			self._headNode = Node(value,self._headNode)

	def backadd(self,value):
		self._bottomNode.setTail(Node(value,None))
		self._bottomNode = self._bottomNode.tail()

	def set(self,value,index):
		i = 0
		while(i <= index):
			self.tail()
			i += 1
		self.head(value)
		self.top()

	def indexadd(self,value,index):
		i = 0
		while(i <= index)
			self.tail()
		self._currentNode().setTail() = Node(value,self._currentNode.tail())
		self.top()


	def frontremove(self):
		rval = self._topNode.head()
		self._topNode = self._topNode.tail()
		return rval

	def backremove(self):
		rval = self._bottomNode.head()
		while(self._currentNode.tail() != self._bottomNode)
			self.tail()
		self._bottomNode = self._currentNode
		self._bottomNode.setTail(None)

		self.top()