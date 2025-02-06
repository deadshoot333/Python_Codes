class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtLast(self,data):
        new_node=Node(data)
        if self.head is Node:
            return new_node 
        tmp=self.head 
        while tmp.next is not None:
            tmp=tmp.next 
        tmp.next=new_node 
        return self.head
    
    def insert(self):
        data=int(input())
        head=self.insertAtLast(data)

    def printList(self):
        tmp=self.head
        print(f'Linked List: ',end="")
        while (tmp) :
            print(f'{tmp.data}',end=" ")
            tmp=tmp.next 
        print("\n")

if __name__=="__main__":
    while 1:
        print("1.Input Number in the Linked List\n2.Print Linked List\n3.Delete Head\n4.Delete Tail")
        choice=int(input("Enter your choice: "))
        ll=LinkedList()
        if choice == 1:
            ll.insert()
        elif choice == 2:
            ll.printList()
        elif choice == 3:
            # Add functionality to delete head
            pass
        elif choice == 4:
            # Add functionality to delete tail
            pass
        else:
            print("Invalid choice")
                
        
    