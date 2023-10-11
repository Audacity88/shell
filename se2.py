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