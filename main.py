from linkedlist import *
from stack import *
from queue import *

def main():

	print("This is the data structures testing tool")
	print("\tto test a stack, input s")
	print("\tto test a queue, input q")

	selection = input("selection: ")

	if(selection == "s"):
		teststack()

	elif(selection == "q"):
		testqueue()
	else:
		print("invalid selection")

main()

