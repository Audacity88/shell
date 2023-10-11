"""
MACS 30111/30121
Short Exercises #2
"""

def peep(p, e):
    """
    Determine whether or not peep = pp^e

    Inputs:
      p (int): first digit
      e (int): second digit

    Returns: True if peep = pp^e, False otherwise
    """

    ### EXERCISE 1 -- Replace pass with your code
    peep = 1001 * p + 110 * e
    pp = 11 * p
    return peep == pp ** e

def has_more(lst1, lst2, target):
    """
    Determine which list contains more of the target value

    Inputs:
      lst1 (list): first list
      lst2 (list): second list
      target: the target value

    Returns: True if lst1 contains more of target, False otherwise
    """

    ### EXERCISE 2 -- Replace pass with your code
    return count_target_in_list(lst1, target) > count_target_in_list(lst2, target)

def count_target_in_list(lst, target):
    """
    Determines how many of the target value a list contains

    Inputs:
      lst (list): list
      target: the target value

    Returns: an integer
    """
    
    count = 0
    for i in lst:
        if i == target:
            count += 1
    return count

def make_star_strings(lst):
    """
    Create a list of star strings

    Input:
      lst (list of nonnegative integers): the list

    Returns: A list of strings of stars (*)
    """

    ### EXERCISE 3 -- Replace pass with your code
    lst2 = []
    for i in lst:
        lst2.append("*" * i)
    return lst2
        
def replace(lst, replacee, replacer):
    """
    Replace one element in a list with another

    Input:
      lst (list): the list
      replacee: the element to replace
      replacer: the element to replace replacee with

    Returns: None, modifies lst in-place
    """

    ### EXERCISE 4 -- Replace pass with your code
    for i in range(len(lst)):
        if lst[i] == replacee:
            lst[i] = replacer

def rows_and_columns_contain(lst, target):
    """
    Determines whether every row and every column of a list
      of lists contains a target value

    lst (list of lists): the list of lists
    target: the target value

    Returns: True if every row and every column of lst contains
      target, False otherwise
    """

    ### EXERCISE 5 -- Replace pass with your code

    if rows_contain(lst, target) and columns_contain(lst, target):
        return True
    else:
        return False

def transpose(lst):
    lst2 = []
    # Since we know the lists are the same length, we can just use the first one
    for i, _ in enumerate(lst[0]):
        newlst = []
        for row in lst:
            newlst.append(row[i])
        lst2.append(newlst)
    return lst2

def rows_contain(lst, target):
    for row in lst:
        if target not in row:
          return False
    return True

def columns_contain(lst, target):
    return rows_contain(transpose(lst), target)