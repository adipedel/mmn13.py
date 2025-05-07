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
