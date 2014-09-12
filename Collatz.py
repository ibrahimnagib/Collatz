__author__ = 'ibrahim'
#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    c_list = [0]*175000

    incrementor = 1
    max_cycle = 0

    if i>j :
        i,j=j,i

    if i < (j/2) :
        i = int(j/2)
    m= (j//2)+1
    if i<m:
        i = m

    for x in range(i,j+1):
        if c_list[x] != 0:
            max_cycle = max(c_list[x], max_cycle)
            continue
        initial_x = x

        while x != 1:
            if (x%2) == 0:
                x = (x//2)
                incrementor += 1
            else:
                x= (3*x+1)//2
                incrementor += 2
            c_list[initial_x] = incrementor

        max_cycle = max(max_cycle, incrementor)
        incrementor = 1

    return max_cycle

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
