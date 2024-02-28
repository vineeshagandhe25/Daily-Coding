# Create a linked list on students marks.

class Node:  # to create a student node
    def __init__(self,name,submarks):
        self.name=name
        self.marks=subjectLinkedlist()
        self.marks.insert(submarks)
        self.next=None

class Marks:  # to create a marks node
    def __init__(self,sub,marks):
        self.sub=sub
        self.marks=marks
        self.next=None

class subjectLinkedlist:  # to create a student's marks linked list
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,submarks) :  # note here submarks is a dict datatype
        for i in submarks:
            newnode=Marks(i,submarks[i])
            if self.head is None:
                self.head=self.tail=newnode
            else:
                self.tail.next=newnode
                self.tail=newnode
    def printlls(self):  # Time Complexity --- O(M) where M is length of submarks
        iter_node=self.head
        while iter_node:
            print(iter_node.sub," ",iter_node.marks)
            iter_node=iter_node.next  

class studentll:  #  to create a student linked list
    def __init__(self): 
        self.head=self.tail=None

    def insert(self,name,submarks):
        if self.head is None:
            self.head=self.tail=Node(name,submarks)
            return
        self.tail.next=Node(name,submarks)
        self.tail=self.tail.next

    def printll(self):  # Time Complexity --- O(N) where N is length of linked list
        iter_node=self.head
        while iter_node:
            print(iter_node.name)
            iter_node.marks.printlls()
            iter_node=iter_node.next
            print("-------")    



marks_data1={'C':100,'C++':100,'JAVA':100,'PYTHON':100,'DBMS':56,'DM':89}
obj=studentll()
obj.insert("alex",marks_data1)    
marks_data2={'C':99,'C++':99,'JAVA':99,'PYTHON':99,'DBMS':95,'DM':98}
obj.insert("bob",marks_data2)  
marks_data3={'C':98,'C++':98,'JAVA':98,'PYTHON':98,'DBMS':85,'DM':96}
obj.insert("caster",marks_data3)  
marks_data4={'C':98,'C++':88,'JAVA':78,'PYTHON':96,'DBMS':95,'DM':94}
obj.insert("dolo",marks_data4)  
marks_data5={'C':100,'C++':98,'JAVA':98,'PYTHON':98,'DBMS':95,'DM':98}
obj.insert("emu",marks_data5)  
marks_data6={'C':89,'C++':87,'JAVA':88,'PYTHON':78,'DBMS':95,'DM':88}
obj.insert("foo",marks_data6)  
marks_data7={'C':100,'C++':98,'JAVA':98,'PYTHON':98,'DBMS':95,'DM':98}
obj.insert("ghu",marks_data7)  
marks_data8={'C':100,'C++':100,'JAVA':100,'PYTHON':100,'DBMS':98,'DM':98}
obj.insert("honey",marks_data8)  
marks_data9={'C':99,'C++':90,'JAVA':97,'PYTHON':96,'DBMS':95,'DM':94}
obj.insert("iron man",marks_data9)  
marks_data10={'C':100,'C++':98,'JAVA':98,'PYTHON':98,'DBMS':95,'DM':98}
obj.insert("jhon",marks_data10)  
obj.printll() 

# *Time Complexity --- O(N) where N is length of linked list
# *Space Complexity ---O(N)  where N is length of linked list


        
