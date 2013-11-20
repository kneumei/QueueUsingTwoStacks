class Stack:
	def __init__(self):
		self.__list=[]
	def push(self, x):
		self.__list.append(x);
	def pop(self):
		return self.__list.pop()
	def peek(self):
		if not self.__list:
			return None
		else:
			return self.__list[-1]

class Queue:
	def __init__(self):
		self.__source = Stack()
		self.__target = Stack()
	def enqueue(self, x):
		if self.__source.peek() == None:
			while self.__target.peek()!=None:
				self.__source.push(self.__target.pop())
		self.__source.push(x)
	def dequeue(self):
		if self.__target.peek() == None:
			while self.__source.peek() != None:
				self.__target.push(self.__source.pop())
		return self.__target.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print q.dequeue()
q.enqueue(4)
q.enqueue(5)
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
