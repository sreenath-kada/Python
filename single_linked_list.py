class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class S_list:
    def __init__(self):
        self.head = None

    def print_list(self):
        print_node = self.head
        print("Here is the list")
        while print_node is not None:
            print(print_node.data)
            print_node = print_node.next

    def insert_AtBegining(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def insert_AtEnd(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        traverse_node = self.head
        while (traverse_node.next):
            traverse_node = traverse_node.next
        traverse_node.next = newNode

    def insert_After(self, data, newData):
        newNode = Node(newData)
        temp_node = self.head
        while temp_node.data is not data:
            temp_node  = temp_node.next
        newNode.next = temp_node.next
        temp_node.next = newNode

    def remove_Node(self, Removedata):
        temp_node = self.head

        if temp_node is not None:
            if temp_node.data == Removedata:
                self.head = temp_node.next
                temp_node = None
                return

        while temp_node is not None:
            if temp_node.data == Removedata:
                break
            prev = temp_node
            temp_node = temp_node.next

        if temp_node is None:
            return

        prev.next = temp_node.next
        temp_node = None


node1 = Node('Mon')
node2 = Node('Tue')
node3 = Node('Wed')

s_list = S_list()
s_list.head = node1
node1.next = node2
node2.next = node3

s_list.print_list()

s_list.insert_AtBegining('Sun')
s_list.print_list()

s_list.insert_AtEnd('Thu')
s_list.print_list()


s_list.insert_After('Tue', 'Fri')
s_list.print_list()

s_list.remove_Node('Wed')
s_list.print_list()
