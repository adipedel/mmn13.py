"""
Author: Adi Pedel
Project: MMN13

This module contains 7 functions that perform various operations on lists and matrices:

1. complement(lst):
   Receives a list of natural numbers and returns a list of the missing natural numbers
   that are smaller than the maximum value in the input list.

2. shift_k_right(lst, k):
   Performs a right circular shift on the input list k times.

3. shift_right_size(a, b):
   Returns the number of right shifts required to make list b equal to list a using shift_k_right.
   Returns None if it's not possible.

4. is_perfect(lst):
   Checks whether traversing the list using the values as indexes covers all elements
   exactly once and returns to index 0.

5. identity_matrix(mat):
   Checks whether a given square matrix is an identity matrix (1s on the diagonal, 0s elsewhere).

6. create_sub_matrix(mat, size):
   Extracts a centered sub-matrix of the specified size from the given square matrix.

7. max_identity_matrix(mat):
   Finds the largest centered sub-matrix of the given matrix that is an identity matrix.
"""

def complement(lst):
    """
        Returns a list of natural numbers missing from the input list,
        where missing numbers are all natural numbers less than the maximum value in lst.

        Parameters:
            lst (list of int): List of natural numbers.

        Returns:
            list of int: Sorted list of natural numbers not present in lst but less than max(lst).
            Returns an empty list if input is empty.
        """
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


def shift_k_right(lst,k):
    """
        Performs a circular right shift on the list k times.

        Parameters:
            lst (list): List of elements to shift.
            k (int): Number of times to shift right.

        Returns:
            list: The list after k right circular shifts.

        Raises:
            ValueError: If k is negative or greater than the length of lst.
        """
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


def shift_right_size(a,b):
    """
        Determines how many right circular shifts are needed on list b to match list a.

        Parameters:
            a (list): Target list.
            b (list): List to be shifted.

        Returns:
            int or None: Number of shifts required to make b equal to a, or None if impossible.
        """
    if len(a) != len(b):    #if the lists lengths are different they can never be equal
        return None
    if a == b:              #if the list are already equal we will return True
        return True
    for i in range (1,len(b)):          #a loop so we will call the function up to the number of the length of the list
        shift_k_right(b,1)          #calling the function with b and 1 (doing shift right 1)
        if a == b:                  #if after the change the lists are equal, the function returns True
            return i
    return None                 #we finished the loop without the lists being equal. returning False


def is_perfect(lst):
    """
        Checks if traversing indices using the values of the list visits all elements exactly once
        and returns to the start index.

        Parameters:
            lst (list of int): List representing indices.

        Returns:
            bool: True if traversal visits every index once and returns to zero, False otherwise.
        """
    if len(lst) == 0:   #an empty list is a perfect list
        return True
    value = 0
    i = 0
    while i < len(lst)-1:       #number of times the loop runs should be the length of the list
        try:
            value = lst[value]      #going to the index that is the value in lst[0]
            if value == 0:          #if value is 0, and we didn't exit the loop, we didn't go through all the indexes
                return False
            i += 1
        except IndexError as err:       #error could be a value that is not in the index range of the list
            print (f"Error detected: {err}")
            return False
        except TypeError as err:        #error could be a value that is not an integer
            print(f"Error detected: {err}")
            return False
    value = lst[value]
    if value == 0:            #if value==0, we went through every index in the list and finished in the correct index
        return True
    else:
        return False

def identity_matrix(mat):
    """
       Checks if a given matrix is an identity matrix.

       Parameters:
           mat (list of lists of int): Square matrix to check.

       Returns:
           bool: True if mat is an identity matrix, False otherwise.

       Raises:
           IndexError: If matrix rows are not equal length (not square).
           TypeError: If any element in the matrix is not an integer.
       """
    mat_size = len(mat)      # the number of rows (and columns) in the square matrix
    if mat_size == 0:
        return False            #empty matrix is not an identity matrix
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


def create_sub_matrix(mat, size):
    """
        Creates a centered sub-matrix of the specified size from the input square matrix.

        Parameters:
            mat (list of lists): Square matrix.
            size (int): Desired size of the sub-matrix (must be <= size of mat).

        Returns:
            list of lists: Centered sub-matrix of dimension size x size.

        Raises:
            IndexError: If matrix rows are not equal length (not square).
        """
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


def max_identity_matrix(mat):
    """
        Finds the size of the largest centered identity sub-matrix within the given matrix.

        Parameters:
            mat (list of lists): Square matrix to search.

        Returns:
            int: Size of the largest identity sub-matrix found, or 0 if none found.

        Prints error messages and returns 0 on exceptions.
        """
    mat_len = len(mat)
    while mat_len != 0:
        try:
            if identity_matrix(mat):  # if we identify an identity matrix, we will return the size of the matrix.
                return mat_len
            elif mat_len == 1:  # if the size of the matrix is 1, and it's not an identity matrix we will return 0
                return 0
            else:
                mat = create_sub_matrix(mat, mat_len - 2)  # trim the matrix by 1 on each side
                mat_len = len(mat)  # the trimmed matrix size
        except (IndexError, TypeError) as err:
            print(f"Error happened: {err}")
            return 0
    return None

