def top_n(items,n):
    """
    Return top n items in an array in descending order
    
    Args:
    items (array): array of items or list
    n (int): number of items to return
    
    Returns:
    array: top n items in descending order
    
    Eg:
    >>> top_n([1,2,3,4,5],3)
    >>> [5,4,3]
    """
    
    for i in range(n):
        for j in range(len(items)-i-1):
            
        if items[j] < items[j+1]:
            items[j], items[j+1] = items[j+1], items[j]
            
    top_n = items[-n:]            
    
    return top_n[::-1]