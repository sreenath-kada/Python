class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def data_insert(self, data):
        if data < self.data:
            if self.left:
                self.left.data_insert(data)
            else:
                self.left = Node(data)
        elif data > self.data:
            if self.right:
                self.right.data_insert(data)
            else:
                self.right = Node(data)

    def data_display(self):
        if self.data:
            if self.left:
                self.left.data_display()
            print(self.data)
            if self.right:
                self.right.data_display()

    def find_entry(self, dataVal):
        if dataVal < self.data :
            if self.left is None:
                return print(str(dataVal) + " Not Found")
            self.left.find_entry(dataVal)
        elif dataVal > self.data :
            if self.right is None:
                return print(str(dataVal) + " Not Found")
            self.right.find_entry(dataVal)
        else:
            print(str(dataVal) + " Found It")


tree = Node(90)
tree.data_insert(50)
tree.data_insert(70)
tree.data_insert(80)
tree.data_insert(65)
tree.data_insert(55)
tree.data_insert(45)
tree.data_insert(30)
tree.data_insert(100)
tree.data_insert(150)
tree.data_insert(10)
tree.data_insert(180)
tree.data_insert(5)
tree.data_insert(155)
tree.data_insert(35)
tree.data_insert(130)
tree.data_insert(200)

tree.data_display()

tree.find_entry(10)
tree.find_entry(201)

