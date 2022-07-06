# Bottom --> 10, 20, 30, 40, 50 --> Top

my_stack = [10, 20, 30, 40, 50]  # List

my_stack.append(60)  # The PUSH OPERATION

print(my_stack)

# New Stack: Bottom ---> 10, 20, 30, 40, 50, 60 ---> Top

my_stack.pop()  # The POP OPERATION

my_stack.pop()  # The same operation 'twice'

print(my_stack)  # From the 'top', 50 and 60 will be removed.

# 'collections' is a package which contains high-performance container datatypes

# 'deque' is a list-like container with fast appends and pops on either end

from collections import deque

# This is your queue. "Roger Federer" is the first to arrive while "Novak Djokovic is the last.

my_queue = deque(["Roger Federer", "Rafael Nadal", "Novak Djokovic"])

my_queue.append("Andre Agassi")  # Now Andre Agassi arrives

my_queue.append("Pete Sampras")  # Now Pete Sampras arrives

print(my_queue)  # You may have a look at the queue below

my_queue.popleft()  # The first to arrives leaves first

my_queue.popleft()  # The second to arrive leaves now

print(my_queue)  # This is your present queue in the order of arrival

# Please Note: At present we are using dictionaries, functions, and loops which have not been taught.

# We will take up all of these concepts in the upcoming units or sections of this course.


# The following code is just to display all the different edges of the graph, as shown in the video lecture.

my_graph = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': [
    'A', 'B', 'D', 'E'], 'D': ['B', 'C', 'E'], 'E': ['D', 'C']}

def define_edges(my_graph):
    edges = []
    for nodes in my_graph:
        for adjacent_nodes in my_graph[nodes]:
            edges.append((nodes, adjacent_nodes))
    return edges


print(define_edges(my_graph))

class Tree:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

    def __str__(self):
        return (str(self.info) + ', Left node: ' + str(self.left) + ', Right node: ' + str(self.right))


tree = Tree("Root Node", Tree("Branch_1", "Leave_1", "Leave_2"),
            Tree("Branch_2", "Leave_3", "Leave_4"))
print(tree)