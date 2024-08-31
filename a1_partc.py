#    Main Author(s): Nehmat Ladhar
#    Main Reviewer(s):



class Stack:

	def __init__(self, cap=10):
		self.capacity_val = cap
		self.stack = [None] * self.capacity_val
		self.top = -1

	def capacity(self):
		# Return the capacity of the stack
		return self.capacity_val

	def push(self, data):
		if self.top + 1 == self.capacity_val:
			self.resize()
		self.top += 1
		self.stack[self.top] = data

	def pop(self):
		if self.is_empty():
			raise IndexError('pop() used on empty stack')
		data = self.stack[self.top]
		self.stack[self.top] = None  #Clear the reference
		self.top -= 1
		return data

	def get_top(self):
		if self.is_empty():
			return None
		return self.stack[self.top]

	def is_empty(self):
		# Check if the stack is empty
		return self.top == -1

	def __len__(self):
		# Return the number of elements in the stack
		return self.top + 1

	def resize(self):
		# Double the capacity of the stack when it is full
		new_capacity = self.capacity_val * 2
		new_stack = [None] * new_capacity
		for i in range(self.capacity_val):
			new_stack[i] = self.stack[i]
		self.stack = new_stack
		self.capacity_val = new_capacity


class Queue:


	def __init__(self, cap=10):
		self.capacity_val = cap
		self.queue = [None] * self.capacity_val
		self.front = 0
		self.size = 0

	def capacity(self):
		# Return the capacity of the queue
		return self.capacity_val

	def enqueue(self, data):
		# Add an element to the back of the queue
		if self.size == self.capacity_val:
			self.resize()
		back = (self.front + self.size) % self.capacity_val
		self.queue[back] = data
		self.size += 1

	def dequeue(self):
		# Rempve and return the oldest value from the front of the queue
		if self.is_empty():
			raise IndexError('dequeue() used on empty queue')
		data = self.queue[self.front]
		self.queue[self.front] = None  #Clear the reference
		self.front = (self.front+1) % self.capacity_val
		self.size -= 1
		return data

	def get_front(self):
		# Get the oldest value from the front of the queue without removing it
		if self.is_empty():
			return None
		return self.queue[self.front]

	def is_empty(self):
		# Check if the queue is empty
		return self.size == 0

	def __len__(self):
		# Return the number of vallues in the queue
		return self.size

	def resize(self):
		# Double the capacity of the queue
		new_capacity = self.capacity_val * 2
		new_queue = [None] * new_capacity
		for i in range(self.size):
			new_queue[i] = self.queue[(self.front + i) % self.capacity_val]
		self.queue = new_queue
		self.capacity_val = new_capacity
		self.front = 0



class Deque:

    def __init__(self, cap=10):
        self.capacity_val = cap
        self.deque = [None] * self.capacity_val
        self.front = 0
        self.size = 0

    def capacity(self):
        # Return the capacity of the dequeue
        return self.capacity_val

    def push_front(self, data):
        if self.size == self.capacity_val:
            self.resize()
        self.front = (self.front - 1) % self.capacity_val
        self.deque[self.front] = data
        self.size += 1

    def push_back(self, data):
        # Add an element to the back of the deque
        if self.size == self.capacity_val:
            self.resize()
        back = (self.front + self.size) % self.capacity_val
        self.deque[back] = data
        self.size += 1

    def pop_front(self):
        # Remove and return the value from the front of the deque
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
        data = self.deque[self.front]
        self.deque[self.front] = None
        self.front = (self.front + 1) % self.capacity_val
        self.size -= 1
        return data

    def pop_back(self):
        # Remove and return the value from the back of the deque
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        back = (self.front + self.size - 1) % self.capacity_val
        data = self.deque[back]
        self.deque[back] = None
        self.size -= 1
        return data

    def get_front(self):
        # Return the value from the front of the deque
        if self.is_empty():
            return None
        return self.deque[self.front]

    def get_back(self):
        # Return the value from the back of the deque
        if self.is_empty():
            return None
        back = (self.front + self.size - 1) % self.capacity_val
        return self.deque[back]

    def is_empty(self):
        # Check if the deque is empty
        return self.size == 0

    def __len__(self):
        # Return the number of values in the deque
        return self.size

    def __getitem__(self, k):
        # Return the k'th value from the front of the deque
        if k < 0 or k >= self.size:
            raise IndexError('Index out of range')
        idx = (self.front + k) % self.capacity_val
        return self.deque[idx]

    def resize(self):
        # Double the capacity of the deque
        new_capacity = self.capacity_val * 2
        new_deque = [None] * new_capacity
        for i in range(self.size):
            new_deque[i] = self.deque[(self.front + i) % self.capacity_val]
        self.deque = new_deque
        self.capacity_val = new_capacity
        self.front = 0
