"""
Laurence Justin Labayen
Lab 3
CS2302 Data Structures
MW 10:30
Professor: Olac Fuentes
TA: Anindita Nath
"""
import math

class Node(object):
    # Constructor
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next 
        
#List Functions
class SortedList(object):   
    # Constructor
    def __init__(self): 
        self.head = None
# Print function prints list's items in order using a loop
    def Print(self):
        t = self.head
        while t is not None:
            print(t.data, end=' ')
            t = t.next
        print() 
    
# Insert function takes self, and a data input as and inserts into the correct
# ascending position in the list            
    def Insert(self, data): 
        n=Node(data)
        # check for empty list  
        if self.head is None: 
            n.next = self.head 
            self.head = n
  
        # check for head at end 
        elif self.head.data >= n.data: 
            n.next = self.head 
            self.head = n 
  
        else: 
            # locate the node before the point of insertion 
            current = self.head 
            while(current.next is not None and
                 current.next.data < n.data): 
                current = current.next
              
            n.next = current.next
            current.next = n 
# Delete function deletes input data "i" and             
    def Delete(self, i):
        t=self.head
        #previous node
        prev=None 
        
        # check if "i" is the head of the list
        if t.data == i:
            self.head = self.head.next
            return
        # iterate through list
        while t is not None and t.data !=i:
            prev = t
            t = t.next
        if t is None:
            return
        # fix list to ascending order
        prev.next=t.next
        t = None
    
    def Merge(self, M):
        #first list
        t=self.head
        #second list
        t2=M.head
        #new list to add sorted elements from first and second list
        t3=Node(None)
        
        #iterate through both lists
        while t is not None and t2 is not None:
            
             #check if current data in the first list is less than
             #the second. if it is, add current element in the first
             #list to the new list
            if t.data <= t2.data:
                t3.next=t
                t=t.next
            #otherwise, element in the second list gets added to new list
            else:
                t3.next=t2
                t2=t2.next
            t3=t3.next
            
            #once we reach end of the list, append the other list
            if t == None:
                t3.next = t2
            elif t2 == None:
                t3.next = t
    
    #IndexOf takes an input "i" and returns the element at index of "i"
    def IndexOf(self, i):
        
        t=self.head
        count=0
        
        #iterate through list
        while t is not None:
            #once current data matches "i", it will return count number
            if t.data==i:
                return print(count)
            else:
                t=t.next
                #add 1 to count for every iteration
                count+=1
        #return -1 if "i" is not in the list
        return print(-1)
            
    #Clear function will delete all elements in the list
    def Clear(self):
        #check if the list is empty
        if self.head is None:
            return
        #otherwise, delete the list by assigning None to self's head
        self.head=None
    
    #Min returns the minimum value in the list
    def Min(self):
        #check if the list is empty
        if self.head is not None:
            #return the first element in the sorted list
            return print(self.head.data)
        #if the list is empty, it returns math.inf
        else:
            return print(math.inf)
    #Max returns the maximum value in the list
    def Max(self):
        
        #check if list is empty, return math.inf if it is
        if self.head is None:
            return print(math.inf)
        #have two pointers, one with current node
        #and one with previous
        t=self.head.next
        prev=self.head
        
        #iterate through list
        while t is not None:
            t=t.next
            prev=prev.next
        #return the last element of the list(prev.data)
        return print(prev.data)
    
    #This function checks if the list has duplicates
    def HasDuplicates(self):
        
        #check if the list is empty
        if self.head is None:
            return print('Empty List')
        
        #have two pointers of nodes next to each other (since
        #list is always sorted)
        t=self.head
        #t2 is ahead by one element
        t2=self.head.next
        
        #iterate through the list
        while t2 is not None:
            #check if the elements are matching
            if t.data==t2.data:
                return print(True)
            else:
                #move both pointers
                t=t.next
                t2=t2.next
        #if the loop has reached the end, then there are no duplicates
        return print(False)
    
    #This function takes k as an input for the kth element in the list
    def Select(self, k):
        
        t=self.head
        count=0
        
        #iterate through the list
        while t is not None:
            #check if the kth element is equal to count
            if k == count:
                #return the data
                return print(t.data)
            #otherwise, keep going through the list and add 1 to count
            else:
                t=t.next
                count+=1
        #once the loop has reached the end, the kth element is
        #not in the list. return math.inf
        return print(math.inf)
            
L=SortedList()
L2=SortedList()
L3=SortedList()

L.Insert(0)
L.Insert(1)
L.Insert(2)
L.Insert(3)

L2.Insert(4)
L2.Insert(8)
L2.Insert(8)
L2.Insert(6)

print('Print L1:',end=' ')
L.Print()
print('Print L2:',end=' ')
L2.Print()
print('')

print('Merge:',end=' ')
L.Merge(L2)
L.Print()

print('Delete #6:',end=' ')
L.Delete(6)
L.Print()

print('IndexOf #8:',end=' ')
L.IndexOf(8)
#L.Clear()
print('Min:',end=' ')
L.Min()

print('Max:',end=' ')
L.Max()
#L.Clear()
print('HasDuplicates:',end=' ')
L.HasDuplicates()


print('Select #2:',end=' ')
L.Select(2)

print('Clear:',end=' ')
L.Clear()
L.Print()
