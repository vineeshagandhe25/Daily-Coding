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

# code to find topper in the class
def topper(obj):
    total=0  # used for total marks of a student
    top=0  # uesd for top marks
    name='' # used for topper name
    iter_node=obj.head  # node to traverse student Linked List

    while iter_node :   # Time Complexity --- O(N) where N is length of linked list
        marks_node=iter_node.marks.head   # node to traverse subject Linked List
        
        while marks_node:  # Time Complexity --- O(M) where M is length of submarks
            total+=marks_node.marks
            marks_node=marks_node.next

        if total > top :  # finding topper
            top=total
            name=iter_node.name

        total=0
        iter_node=iter_node.next

    return name  # returning topper name    

# function to get avg marks at subject level
def avg_marks_at_sub(obj):
    sub_marks={'C':0,'C++':0,'JAVA':0,'PYTHON':0,'DBMS':0,'DM':0}
    iter_node=obj.head  # node to traverse student Linked List

    while iter_node :   # Time Complexity --- O(N) where N is length of linked list

        marks_node=iter_node.marks.head   # node to traverse subject Linked List
        
        while marks_node:  # Time Complexity --- O(M) where M is length of submarks
            sub_marks[marks_node.sub] += marks_node.marks
            marks_node=marks_node.next

        iter_node=iter_node.next
    # to find avg 
    for i in sub_marks:
        sub_marks[i] //= 10

    return sub_marks       

# function to get list of failed students
def failed_students(obj):
    names=[] # used for failed names
    iter_node=obj.head  # node to traverse student Linked List

    while iter_node :   # Time Complexity --- O(N) where N is length of linked list
        marks_node=iter_node.marks.head   # node to traverse subject Linked List
        
        while marks_node:  # Time Complexity --- O(M) where M is length of submarks
            if marks_node.marks < 40:
                names.append(iter_node.name)
            marks_node=marks_node.next

        iter_node=iter_node.next

    return names  

# function to sort subjects based on their avg score
def sort_avg_score(obj):
    avg_marks=avg_marks_at_sub(obj)
    sort_avg_marks=dict(sorted(avg_marks.items(),key=lambda item:item[1]))
    return sort_avg_marks

# function to sort students based on their total marks
def sort_students(obj):
    iter_node=obj.head  # node to traverse student Linked List
    total=0
    students=[]

    while iter_node :   # Time Complexity --- O(N) where N is length of linked list

        marks_node=iter_node.marks.head   # node to traverse subject Linked List
        
        while marks_node:  # Time Complexity --- O(M) where M is length of submarks
            total += marks_node.marks 
            marks_node=marks_node.next
        
        students.append([iter_node.name,total])
        iter_node=iter_node.next
        total=0
    
    # sorting
    for i in range(len(students)):
        for j in range(len(students)-i-1):
              if students[j][1] < students[j+1][1] :
                  students[j][1],students[j+1][1]=students[j+1][1],students[j][1]  
 

    return students           



marks_data1={'C':100,'C++':100,'JAVA':100,'PYTHON':100,'DBMS':100,'DM':99}
obj=studentll()
obj.insert("alex",marks_data1)    
marks_data2={'C':99,'C++':99,'JAVA':99,'PYTHON':99,'DBMS':95,'DM':98}
obj.insert("bob",marks_data2)  
marks_data3={'C':98,'C++':98,'JAVA':98,'PYTHON':98,'DBMS':85,'DM':96}
obj.insert("caster",marks_data3)  
marks_data4={'C':98,'C++':88,'JAVA':78,'PYTHON':96,'DBMS':95,'DM':94}
obj.insert("david",marks_data4)  
marks_data5={'C':100,'C++':98,'JAVA':98,'PYTHON':98,'DBMS':95,'DM':98}
obj.insert("emu",marks_data5)  
marks_data6={'C':89,'C++':87,'JAVA':88,'PYTHON':78,'DBMS':95,'DM':88}
obj.insert("foo",marks_data6)  
marks_data7={'C':100,'C++':98,'JAVA':98,'PYTHON':98,'DBMS':95,'DM':98}
obj.insert("ghu",marks_data7)  
marks_data8={'C':100,'C++':100,'JAVA':100,'PYTHON':100,'DBMS':98,'DM':98}
obj.insert("honey",marks_data8)  
marks_data9={'C':99,'C++':90,'JAVA':97,'PYTHON':39,'DBMS':95,'DM':94}
obj.insert("imrean",marks_data9)  
marks_data10={'C':100,'C++':100,'JAVA':100,'PYTHON':100,'DBMS':100,'DM':100}
obj.insert("jhon",marks_data10)  
#obj.printll() 
print('The topper ---',topper(obj))
print('avg marks at sub level',avg_marks_at_sub(obj))
print('Failed students :',failed_students(obj))
print('sorted avg max ',sort_avg_score(obj))
print('sorted students ',sort_students(obj))


# *Time Complexity --- O(N) where N is length of linked list
# *Space Complexity ---O(N)  where N is length of linked list


        
