"""
Name: Adi Pedel
Project: mmn13 contains 7 functions.
1.complement receives a list of numbers and returns the natural numbers that are not on the list and are smaller
than the max number in the received list.
2.shift_k_right receives a list of number and a number k. it performs shift k right on the list.
3.shift_right_size receives two lists of numbers and checks how many shift rights it takes to make them equal
(if possible) using the shift_k_right function.
4.is_perfect checks if doing a scan by cell values of the list will go through all the cells.
5.identity_matrix receives a matrix (using a two-dimensional list) and checks if it's an identity matrix.
6.create_sub_matrix receives a matrix and a size and returns a sub matrix with the received size (following the center of the matrix)
7.max_identity_matrix receives a matrix and using the functions identity_matrix and create_sub_matrix, checks whats
is thr max sub matrix that is a identity matrix(following the center of the matrix)
"""

""""
complement is a function that receives a list of natural numbers, it checks what is the max value in the list,
and goes through every natural number up to that number and checks if it on the list. every number that is not on
the list will be added to a new list. in the end the function will return the new list.
"""
def complement(lst):
    new_lst = []
    list_len = len(lst)
    if list_len == 0:                #empty list
        return lst
    for number in range(1,max(lst)):  #going through the natural numbers from 1 to the max value of the given list
        i = 0
        for list_num in lst:              #going through the given list
            i += 1
            if number == list_num:         #checking if the number is equal to the number in the list
                break
            if i == list_len:                #the number is not on the list
                new_lst.append(number)      #adding the number to the new list
    return new_lst

"""
shift_k_right is a function that receives a list of numbers and a number k. it does a shift right k times using a
 loop that runs k times. on each loop it goes through the list a replaces the value of list[i] with the value of
 list[i-1]. The function returns the updated list.
 """
def shift_k_right(lst,k):
    if k < 0 or k > len(lst):
        raise ValueError("k must be between 0 and the length of the list.")
    previous_num = lst[0]        # saving the value of the first item on the list so we won't overwrite it.
    for i in range(0,k):        #the outer loop for the shift right to be done k times
        for j in range(len(lst)):       #the inner loop that goes through the list
            if j==0:
                lst[0] = lst[-1]        #updating the first item to have the value of the last one
            else:
                temp = lst[j]           #saving the value of the item on the list so we won't overwrite it.
                lst[j] = previous_num   #updating the item to have the value of the last one we saved
                previous_num = temp     #saving the previous value of the item for the next item
    return lst

"""
shift_right_size is a function that receives 2 list a,b. by using the function shift_k_right it checks if after
doing shift right on list b the 2 lists are equal. it does it by sending the list b and the number 1 to the function
and each time checks if a and the updated b list are equal. the function calls the function up to the number of the 
 length of the list (after that b list resets). the function returns True if it possible to make the lists equal
 by using the function, and False if its not possible.
 """
def shift_right_size(a,b):
    if len(a) != len(b):    #if the lists lengths are different they can never be equal
        return None
    if a == b:              #if the list are already equal we will return True
        return True
    for i in range (1,len(b)):          #a loop so we will call the function up to the number of the length of the list
        shift_k_right(b,1)          #calling the function with b and 1 (doing shift right 1)
        if a == b:                  #if after the change the lists are equal, the function returns True
            return i
    return None                 #we finished the loop without the lists being equal. returning False
