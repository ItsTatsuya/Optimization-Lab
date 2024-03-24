# sequencing problem

import numpy as np

def sequencing(c, A, b):
    m, n = A.shape
    c = np.array(c)
    A = np.array(A)
    b = np.array(b)
    c = np.concatenate((c, np.zeros(m+n)))
    A = np.concatenate((A, np.eye(m)), axis=1)
    A = np.concatenate((A, np.eye(n)), axis=1)
    c = -c
    n = len(c)
    m = len(b)
    N = list(range(n))
    B = list(range(n, n+m))
    while True:
        # find entering variable
        j = np.argmax(c)
        if c[j] <= 0:
            break
        # find leaving variable
        i = None
        for k in range(m):
            if A[k, j] > 0:
                if i is None or b[k]/A[k, j] < b[i]/A[i, j]:
                    i = k
        if i is None:
            raise ValueError('unbounded')
        # pivot
        A[i] /= A[i, j]
        b[i] /= A[i, j]
        for k in range(m):
            if k != i:
                A[k] -= A[k, j]*A[i]
                b[k] -= A[k, j]*b[i]
        c -= c[j]*A[i]
        N[j], B[i] = B[i], N[j]
    return c[-m:], b

def main():
    c = [2, 3]
    A = np.array([[1, 1], [2, 1], [1, 0]])
    b = [4, 7, 3]
    print(sequencing(c, A, b))
    
if __name__ == '__main__':
    main()
    