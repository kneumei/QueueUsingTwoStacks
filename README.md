Implement a queue using two stacks
=============

A [queue](http://en.wikipedia.org/wiki/Queue) is a collection which takes the value being inserted and puts it at the end of the collection (or line).  The queue works using a first in first out (FIFO) order.  A [stack](http://en.wikipedia.org/wiki/Stack) is a collection which takes the value being inserted and puts it at the top of the collection.  The stack works using a last in first out (LIFO) order which is the opposite of a queue.  For this code kata we are going to implement a queue using two stacks.

###TASK
Implement the following methods for your queue class (FIFO):
* **void Enqueue(int value)** - this method adds the value to the front of the queue.
* **int Dequeue()** - this method will get the value from the front of the queue and remove it from the list.
* **Note:** Use two stacks to implement the internals of the queue.

Implement the following methods for your stack class (LIFO):
* **void Push(int value)** - this method adds the value to the top of the stack.
* **int Pop()** - this method gets the value from the top of the stack and removes it from the list.

Use whatever programming language you prefer to solve this problem.

###INPUT
Use the following items as example inputs:
* queue.Enqueue(1);
* queue.Enqueue(2);
* queue.Enqueue(3);
* queue.Dequeue();
* queue.Enqueue(4);
* queue.Enqueue(5);
* queue.Dequeue();
* queue.Dequeue();
* queue.Dequeue();
* queue.Dequeue();

###OUTPUT
These are the outputs you should expect from the above inputs:
* queue = { 1 }
* queue = { 1, 2 }
* queue = { 1, 2, 3 }
* Dequeue method returns 1, queue = { 2, 3 }
* queue = { 2, 3, 4 }
* queue = { 2, 3, 4, 5 }
* Dequeue method returns 2, queue = { 3, 4, 5}
* Dequeue method returns 3, queue = { 4, 5 }
* Dequeue method returns 4, queue = { 5 }
* Dequeue method returns 5, queue = { }

####REFERENCE
[David Hudson](https://davidhudson.me) and I were discussing this very problem over lunch last week.  He even mentioned that it would be a good code kata and I agreed 100%.  Thanks, [David](https://twitter.com/_davidhudson)!

### Answer Submission Instructions
1. Fork this repository.
2. Write your solution to the problem.
3. Commit your solution to your forked repository.
4. Post a link to your fork as a comment to the [Queue using two stacks post](http://codekata.co/2013/11/03/queue-using-two-stacks/).

