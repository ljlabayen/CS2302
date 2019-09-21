"""
Laurence Justin Labayen
Lab 2
CS2302 Data Structures
MW 10:30
Professor: Olac Fuentes
TA: Anindita Nath
"""
import random
import time

#select_bubble recusively sorts adjacent elements and swaps them
#to the correct ascending position in the list
#It takes k as an input and returns the kth element of the list
def select_bubble(L, end, k):
    swapped=False
    #base case if list is sorted
    if end <= 0:
        return L[k]
    
    for i in range(0, end):
         #compares adjacent elements
        if(L[i + 1] < L[i]):
             #swap elements
            L[i + 1], L[i] = L[i], L[i + 1]
            swapped=True  
     #if elements are swapped, recusively call select_bubble        
    if swapped==True:
        #recursive call with last element removed
        return select_bubble(L, end - 1, k)   
     
    return L[k]

#partition selects pivot and compares elements to be placed on the left or
#right side of the pivot 
#input: list, start of list, and end of list
#output: index of pivot
def partition(L, start, end):
    i = (start-1)
    pi=L[end] #pivot is selected to be the last element
    
    for j in range(start, end):
        if L[j] <= pi: #check if element at j is less than or equal to pivot
            i = i+1 #increment i
            L[i],L[j] = L[j],L[i] #swap elements
    
    L[i+1],L[end] = L[end],L[i+1] #move pivot to correct position in the list
    
    return (i+1) #return pivot index

#select_quick is a standard recursive quick sort function. Calls partition and 
#uses the returned pivot index to create and sort 2 sublists to the left and
#right of pivot
#input: list, start of list, and end of list, kth index of sorted list
#output: kth element of list
def select_quick(L, start, end, k):
    #base case
    if start < end:
        #calling partition to return pivot of partitioned list
        pi = partition(L, start, end)
        #left of pivot call
        select_quick(L, start, pi-1, k)
        #right of pivot call
        select_quick(L, pi+1, end, k)
    
    return L[k]
#select_modified_quick is similar to standard quicksort except, it only 
#recusively calls the sublist where the kth element is
#input: list, start of list, and end of list, kth index of sorted list
#output: kth element of list
def select_modified_quick(L, start, end, k):
    #calling partition to return pivot of partitioned list
    pi = partition(L, start, end)
    
    #check if pi is the kth element. end recursion
    if k == pi:
        L[pi]
    #check if k is in the left sublist
    if k < pi:
        return select_modified_quick(L, start, pi-1, k)
    #otherwise, k must be in right sublist
    else:
        return select_quick(L, pi+1, end, k)

class stackRecord:
    def __init__(self, L, start, end):
        self.L = L
        self.start = start
        self.end = end

#select_quick_nr is a non recursive quicksort that uses a stack instead of 
#recursion to sort a given list
#input: list, start of list, and end of list, kth index of sorted list
#output: kth element of list       
def select_quick_nr(L, start, end, k):
    stack = [stackRecord(L, start, end)]
    #loop until stack is at 0
    while(len(stack) > 0):
        #h gets last element
        h = stack.pop(-1)
        if h.start < h.end:
            #pi gets value of pivot
            pi = partition(h.L, h.start, h.end)
            
            #append left and right sublists
            stack.append(stackRecord(h.L, h.start, pi - 1))
            stack.append(stackRecord(h.L, pi + 1, h.end))
    return L[k]
#select_quick_while uses iteration using a while loop instead of recursion.
#This function does not sort the list completely but only sorts the sublist
#where kth element is
#input: list, start of list, and end of list, kth index of sorted list
#output: kth element of list   
def select_quick_while(L, start, end, k):
    #calling partition to return pivot of partitioned list
    pi = partition(L, start, end)
    #iterate through list until k is equal to pivot
    while(pi != k):
        if k < pi:
            pi = partition(L, start, pi -1)
        elif k > pi:
            pi = partition(L, pi + 1, end)
            
    return L[pi]

if __name__=="__main__":
    
    listsize=int(input("Enter list size: "))
    
    k=int(input("Enter kth element: "))
    
    #create a list witht the size entered by user with random elements
    list1 = []
    for i in range(listsize):
        list1.append(random.randint(0, 99))
    #use the same list for each function for consistency    
    L1 = list1
    L2 = list1
    L3 = list1
    L4 = list1
    L5 = list1
    
    #check if user enters invalid input(s)
    if k<listsize and k>=0:
        start = time.perf_counter()
        print('\nselect_bubble kth element is: ', select_bubble(L1, len(L1)-1, k))
        end = time.perf_counter()
        print('select_bubble took ' + str(round((end - start), 5)) + ' seconds\n')
        
        start = time.perf_counter()
        print('\nselect_quick kth element is: ', select_quick(L2, 0, len(L1)-1, k))
        end = time.perf_counter()
        print('select_quick took ' + str(round((end - start), 5)) + ' seconds\n')
      
        start = time.perf_counter()
        print('\nselect_modified_quick kth element is: ', select_modified_quick(L3, 0, len(L1)-1, k))
        end = time.perf_counter()
        print('select_modified_quick took ' + str(round((end - start), 5)) + ' seconds\n')
        
        start = time.perf_counter()
        print('\nselect_quick_nr kth element is: ', select_quick_nr(L4, 0, len(L1)-1, k))
        end = time.perf_counter()
        print('select_quick_nr took ' + str(round((end - start), 5)) + ' seconds\n')
        
        start = time.perf_counter()
        print('\nselect_quick_while kth element is: ', select_quick_while(L5, 0, len(L1)-1, k))
        end = time.perf_counter()
        print('select_quick_while ' + str(round((end - start), 5)) + ' seconds\n')
    else:
        print("kth element is more than list size",
              "\nor you entered an invalid number")
