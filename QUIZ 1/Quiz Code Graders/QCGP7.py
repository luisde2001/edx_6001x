def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    a = 6
    b = 9
    c = 20
    for x in range(0, n):
        for y in range(0, n):
            for z in range(0, n):
                if a*x + b*y + c*z == n:
                    return True
    return False