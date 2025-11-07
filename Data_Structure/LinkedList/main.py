class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtLast(self,data):
        new_node = Node(data)
        if self.head is None: 
            self.head=new_node 
            return 
        current_node = self.head 
        while current_node.next is not None:
            current_node = current_node.next 
        current_node.next=new_node
    
    def insert(self):
        data=int(input())
        self.insertAtLast(data)
    
    def delete_first(self):
        if self.head is None:
            return 
        tmp=self.head 
        self.head=self.head.next 
        del tmp 
    def delete_last(self):
        if self.head is None:
            return 
        if (self.head is not None) and (self.head.next is None):
            self.head=None 
            return 
        current_node=self.head 
        while current_node.next and current_node.next.next is not None: 
            current_node=current_node.next 
        current_node.next=None 
        
    def printList(self):
        tmp=self.head
        print(f'Linked List: ',end="")
        while (tmp) :
            print(f'{tmp.data}',end=" ")
            tmp=tmp.next 
        print("\n")

if __name__=="__main__":
    ll=LinkedList()
    while 1:
        print("1.Input Number in the Linked List\n2.Print Linked List\n3.Delete Head\n4.Delete Tail")
        choice=int(input("Enter your choice: "))
        if choice == 1:
            ll.insert()
        elif choice == 2:
            ll.printList()
        elif choice == 3:
            ll.delete_first()
        elif choice == 4:
            ll.delete_last()
        else:
            print("Invalid choice")
                
        
    