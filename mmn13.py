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
                lst[j],previous_num = previous_num,lst[j]
#updating the item to have the value of the last one we saved and updating previous_num to the value of the item right now
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

"""
is_perfect is a function that receives a list of numbers. it starts with the number 0 and checks for the value
in list[0], it takes the value and checks what's the value in that index on the list and so on. the function checks
if by doing that we can reach each index on the list and finish in index 0. It does it with a while loop that runs no
more times than the list length. If the loop detects the value 0 before we went through all the indexes we will
return False, and if we exited the loop and the value isn't 0 we will return False. In an other case, the list is
perfect and we will return True.
"""
def is_perfect(lst):
    if len(lst) == 0:   #an empty list is a perfect list
        return True
    value = 0
    i = 0
    while i < len(lst)-1:       #number of times the loop runs should be the length of the list
        try:
            value = lst[value]      #going to the index that is the value in lst[0]
            if value == 0:          #if value is 0 and we didn't exit the loop, we didn't go through all the indexes
                return False
            i += 1
        except IndexError as err:       #error could be a value that is not in the index range of the list
            print (f"Error detected: {err}")
            break
        except TypeError as err:        #error could be a value that is not an integer
            print(f"Error detected: {err}")
            break
    value = lst[value]
    if value == 0:            #if value==0, we went through every index in the list and finished in the correct index
        return True
    else:
        return False

"""
identity_matrix is a function that receives a matrix and checks if it's an identity matrix.
It does this using nested loops over the rows and columns. It checks that all elements on the main diagonal are 1,
and all other elements are 0. The function returns True if the matrix is an identity matrix, and False otherwise.
"""
def identity_matrix(mat):
    mat_size = len(mat)      # the number of rows (and columns) in the square matrix
    for row in mat:
        if len(row) != mat_size:        #checks if the matrix is square
            raise IndexError("Not all rows are equal")
    for row in range (mat_size):              #loop over rows
        for column in range (mat_size):        #loop over column
            if type(mat[row][column]) != int:
                raise TypeError("Not all values are int")
            if (row == column and mat[row][column] != 1) or (row != column and mat[row][column] != 0):
                # check that diagonal elements are 1 and all others are 0
                return False
    return True

""" 
create_sub_matrix is a function that receives a matrix and a size that is less than or equal to the size of the matrix,
and creates a sub-matrix of that size from the given matrix. The function first calculates the size of the matrix and 
then the difference between the matrix size and the given size. It creates a new matrix by trimming half of the 
difference from each side of the matrix. The function returns the new sub-matrix.
"""
def create_sub_matrix(mat, size):
    mat_len = len(mat)
    sub_mat = []                #create the new matrix (with a two-dimensional list)
    for row in mat:
        if len(row) != mat_len:         # check that the matrix is square
            raise IndexError("Not all rows are equal")
    size_difference = mat_len - size
    if size_difference == 0:                #if sizes are equal, return the original matrix
        return mat
    else:
        sub_mat_row = 0
        for row in range (size_difference//2, mat_len-size_difference//2):
            # we add rows to the new matrix, skipping half of the size difference from top and bottom
            sub_mat.append([])                  #create a new row in the sub-matrix
            for column in range (size_difference//2, mat_len-size_difference//2):
                # we add columns to the new row, skipping half of the size difference from left and right
                sub_mat[sub_mat_row].append(mat[row][column])
            sub_mat_row += 1
    return sub_mat

"""
max_identity_matrix is a function that receives a matrix and returns the size of the largest identity matrix
that can be obtained by trimming the original matrix. It uses the identity_matrix function to check if the current
matrix is an identity matrix, and the create_sub_matrix function to trim the matrix by 1 on each side.
The function returns the size of the first identity matrix we identify.
"""
def max_identity_matrix(mat):
    mat_len = len(mat)
    while mat_len != 0:
        try:
            if identity_matrix(mat):        #if we identify an identity matrix, we will return the size of the matrix.
                return mat_len
            elif mat_len == 1:        #if the size of the matrix is 1, and it's not an identity matrix we will return 0
                return 0
            else:
                mat = create_sub_matrix(mat, mat_len-2)         #trim the matrix by 1 on each side
                mat_len = len(mat)                          #the trimmed matrix size
        except (IndexError, TypeError) as err:
            print (f"Error happened: {err}")
            return 0