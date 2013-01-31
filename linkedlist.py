from node import Node

class LinkedList:

	def __init__(self,value = None):
		# if no value is passed in
		if(value == None):
			self._size = 0
			self._headNode = None
			self._tailNode = None
		else:
			self._headNode = Node(value,None)
			self._tailNode = self._headNode
			self._size = 1

	def get(self,index):
		if(index == 0):
			return self._headNode.head()
		elif(index == self._size - 1):
			return self._tailNode.head()
		else:
			i = 0
			walk = self._headNode
			while(i < index):
				walk.tail()
			return walk.head()

	def frontadd(self,value):
		self._headNode = Node(value,self._headNode)
		# if the headNode has tail None (is the last node)
		# then it IS tailNode
		if(self._headNode.tail() == None):
			self._tailNode = self._headNode
		self._size += 1

	def backadd(self,value):
		if(self._headNode == None):
			self.frontadd(value)
			return
		self._tailNode.setTail(Node(value,None))
		self._tailNode = self._tailNode.tail()
		self._size += 1

	def frontremove(self):
		rval = self._headNode.head()
		self._headNode = self._headNode.tail()
		self._size -= 1
		return rval

	def backremove(self):
		rval = self._tailNode.head()
		walk = self._headNode()

		while(walk.tail() != self._tailNode):
			walk = walk.tail()

		self._tailNode = walk
		self._tailNode.setTail(None)
		self._size -= 1

		return rval

	def extract(self):
		if(self._headNode == None):
			return []
		rlist = []
		walk = self._headNode
		while(walk.tail() != None):
			rlist.append(walk.head())
			walk = walk.tail()
		rlist.append(walk.head())

		return rlist
