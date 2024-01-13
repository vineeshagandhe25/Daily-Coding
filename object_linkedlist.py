    
class Student:
    def _init_(self,name,roll,status):
        self.name=name
        self.roll=roll
        self.status=status
    def display(self):
        print("Name: ",self.name)
        print("Rollno ",self.roll)
        print("Status: ",self.status)
class Node:
    def _init_(self,obj):
        self.data=obj
        self.next=None
class classlist:
    def _init_(self):
        self.head=None
    def add(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=newnode
    def printd(self):
        temp=self.head
        while temp is not None:
            print(temp.data.display())
            temp=temp.next
s=Student("vineesha",308,"Running")
s2=Student("vinni",803,"passedOut")
l=classlist()
l.add(s)
l.add(s2)
l.printd()

