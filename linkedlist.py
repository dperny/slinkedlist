from node import Node

def testllist():

    size = input("input the size of the dynamic circular array: ")
    x = LinkedList(int(size))

    #options block. shows commands

    operation = "h"
    FLAG = True
    i = 0

    while(operation != "q"):

        op = input("input operation: ")
        operation = operation if (op == "") else op

        if(operation == "_F"):
            FLAG = not FLAG
            continue

        elif(operation == "h"):
            print("Options: \n\tg to get at index \n\ts to set at index")
            print("\tba to add to back\n\tfa to add to front")
            print("\tbr to remove from back\n\tfr to remove from front")
            print("\tir to remove from index\n\te to extract")
            print("\tie for isEmpty\n\tif for isFull")
            print("\tsi for size\n\tr for repeat last command")
            print("\t_F to toggle sequential (quick) data\n\tq to quit")
            continue

        elif(operation == "g"): 
            index = int(input("index: "))

            try:
                rval = x.get(index)
            except IndexError:
                print("index is out of bounds")
                continue

            print("index {0} is {1}".format(index,rval))
            continue

        elif(operation == "fr"):
            print("value {0} was removed from the front".format(x.frontremove()))
            continue

        elif(operation == "br"):
            print("value {0} was removed from the back".format(x.backremove()))
            continue

        elif(operation == "ir"): 
            index = int(input("index: "))
            try:
                print("value {0} was removed from index{1}".format(x.indexremove(index),index))
            except IndexError:
                print("invalid index")
            continue

        elif(operation == "e"):
            print(x.extract())
            continue

        elif(operation == "ie"):
            print("array is empty") if x.isEmpty() else print("array not empty")
            continue

        elif(operation == "if"):
            print("array is full") if x.isFull() else print("array not full")
            continue

        elif(operation == "si"):
            print("size of the array is {0}".format(x.size()))
            continue

        # datum is i (increment i each time) if sequential mode is on
        # else get user input
        if FLAG: datum = i; i += 1
        else: datum = input("input datum: ")

        if(operation == "s"):
            index = int(input("index: "))
            try:
                x.set(index,datum)
            except IndexError:
                print("index is out of bounds")
                continue

        elif(operation == "ba"):
            x.backadd(datum)
        elif(operation == "fa"):
            x.frontadd(datum)
        elif(operation == "ia"):
        	index = int(input("index: "))
        	try:
        		x.indexadd(index,datum)
        	except IndexError:
        		print("index is out of bounds")
        else:
            print("invalid option")

    return

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
		self._verifyIndex(index)
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

	def set(self,index,value):
		self._verifyIndex(index)
		i = 0
		walk = self._headNode
		while(i < index):
			walk.tail()
		walk.setHead(value)

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

	def indexadd(self,index,value):
		if(index == 0):
			self.frontadd(value)
			return
		self._verifyIndex(index)
		i = 0
		walk = self._headNode
		while(i < index-1):
			walk.tail()
		walk.setTail(Node(value,walk.tail()))

	def indexremove(self,index):
		if(index == 0):
			self.frontremove()
			return
		self._verifyIndex(index)
		i = 0
		walk = self._headNode
		while(i < index-1):
			walk.tail()
		rval = walk.tail().head()
		walk.setTail(walk.tail().tail())
		return rval

	def frontremove(self):
		rval = self._headNode.head()
		self._headNode = self._headNode.tail()
		self._size -= 1
		return rval

	def backremove(self):
		rval = self._tailNode.head()
		walk = self._headNode

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

	def _verifyIndex(self,index):
		if(index > self._size-1):
			raise IndexError("index out of bounds")
		else: return








testllist()