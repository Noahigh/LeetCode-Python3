"""
参考文章： https://www.cnblogs.com/king-ding/p/pythonchaintable.html

作者：陈栋权

时间：2016/09/19

本文版权归作者和博客园共有，欢迎转载，但未经作者同意必须保留此段声明，

且在文章页面明显位置给出原文连接，否则保留追究法律责任的权利。

如有特别用途，请与我联系邮箱：kingchen.gd@foxmail.com
"""
class Node:
    def __init__(self, data=None):
        """
        初始化链表节点
        """
        self.data = data
        self.next = None

class LinkedNode:
    def __init__(self):
        self._head = None
        self.length = 0
    
    # 判断链表是否为空
    def is_Empty(self):
        return self.length == 0
    
    # 链表尾部增加节点
    def add_Node(self, data):
        item = None
        # 判断传进来的参数是否为链表节点
        if isinstance(data, Node):
            item = data
        else: # 如果不是，则初始化该节点
            item = Node(data)
        
        # 判断是否存在头指针
        if not self._head: # 如果不存在，则头指针指向当前链表节点
            self._head = item
            self.length += 1
        else:
            current_node = self._head
            # 使用while循环，到达已存在链表的最后一个节点处
            while current_node.next:
                current_node = current_node.next
            # 将已存在的链表的最后一个节点的next指向新的节点
            current_node.next = item
            self.length += 1
        
    # 按索引位置删除节点（注意链表长度减1）
    def del_Node(self, index):
        # 考虑链表为空的情况
        if self.is_Empty():
            print("Error: The 'LinkedList' is empty!")
            return
        # 考虑索引越界的问题
        if index < 0 or index >= self.length:
            print("Error: Out of index.")
            return 
        # 考虑删除第一个节点的情况
        if index == 0:
            self._head = self._head.next
            self.length -= 1
            return

        # current_node: 当前节点
        # previous_node: 前导节点
        i = 0
        current_node = self._head
        previous_node = self._head
        # 循环找到要删除的索引位置的节点信息
        while current_node.next and i < index:
            previous_node = current_node
            current_node = current_node.next
            i += 1
        
        if i == index:
            previous_node.next = current_node.next
            self.length -= 1

    # 更新链表节点
    def update_Node(self, index, data):
        # 判断是否符合条件
        if self.is_Empty() or index < 0 or index >= self.length:
            print("Error: Out of index.")
            return
        i = 0
        current_node = self._head
        while current_node.next and i < index:
            current_node = current_node.next
            i += 1
        
        if i == index:
            current_node.data = data

    # 按索引查找链表节点，返回节点内容
    def get_Data(self, index):
        if self.is_Empty() or index < 0 or index >= self.length:
            print("Error: Out of index.")
            return
        i = 0
        current_node = self._head
        while current_node.next and i < index:
            current_node = current_node.next
            i += 1
        print(current_node.data)
        return

    # 按内容查找链表节点，返回节点索引
    def get_Index(self, data):
        if self.is_Empty():
            print("Error: The 'LinkedList' is empty!")
            return
        i = 0
        current_node = self._head
        while i < self.length:
            if current_node.data == data:
                print(i)
                return
            current_node = current_node.next
            i += 1
        print("Error: The LinkedList has no data like: " + str(data) + ".")

    # 插入链表节点
    def insert_Node(self, index, data):
        # 判断链表是否为空链表
        if self.is_Empty():
            print("Error: The 'LinkedList' is empty!")
            return
        # 判断索引是否越界
        if index < 0 or index >= self.length:
            print("Error: Out of index.")
            return
        item = None
        
        if isinstance(data, Node):
            item = data
        else:
            item = Node(data)
        
        if index == 0:
            item.next = self._head
            self._head = item
            self.length += 1
            return

        i = 0
        previous_node = self._head
        current_node = self._head
        while current_node.next and i < index:
            previous_node = current_node
            current_node = current_node.next
            i += 1
        if i == index:
            item.next = current_node
            previous_node.next = item
            self.length += 1        

    # 翻转链表
    def reserve_LinkedList(self):
        # 判断链表是否为空
        if self.is_Empty():
            print("Error: The 'LinkedList' is empty!")
            return
        
        # 如果链表长度为1，直接返回链表本身就可以
        if self.length == 1:
            return
        
        i = 1
        # previous_node = self._head
        # current_node = self._head.next
        # next_node = self._head.next
        
        next_node = self._head
        previous_node = next_node
        current_node = next_node.next
        next_node = next_node.next

        # 链表的第一个节点特殊处理，next-->None
        previous_node.next = None

        while i < self.length:
            next_node = next_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            i += 1
        self._head = previous_node

    # 清空当前链表
    def clear_LinkedList(self):
        if self.is_Empty():
            print("Error: The 'LinkedList' is empty!")
            return
        self._head = Node
        self.length = 0

    # 以类似 1 --> 2 --> 3 的形式展示列表
    def show(self):
        if self.is_Empty():
            print("Error: The 'LinkedList' is empty!")
            return
        print("The LinkedList like: ")
        current_node = self._head
        while current_node.next:
            print(current_node.data, end='')
            print(" --> ", end='')            
            current_node = current_node.next
        print(current_node.data)
        return

# 测试部分
a = LinkedNode()
b = Node(1)
c = 2
d = 3

a.add_Node(b)
a.show()
a.add_Node(c)
a.add_Node(d)
a.show()
a.del_Node(2)
a.show()
print("The LinkedNode's data is:")
a.get_Data(1)
a.get_Data(5)
print("The LinkedNode's index is:")
a.get_Index(2)
a.get_Index(3)
a.update_Node(0, 5)
a.show()

print("Reverse the LinkedList: ")
a.reserve_LinkedList()
a.show()
a.add_Node(9)
a.show()
a.reserve_LinkedList()
a.show()
a.add_Node(10)
a.show()
a.reserve_LinkedList()
a.show()




        
