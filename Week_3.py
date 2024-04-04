#이론문제

#1 => O
#2 => O
#3 => X 고정
#4 => O
#5 => X 그건 vstack


#실습문제

import numpy as np

#1
Hit = 0
Try = 1
while Hit == 0:
    a = np.random.randint(low = -100, high = 101, size = (1,3))
    b = np.random.randint(low = -100, high = 101, size = (1,3))
    c = np.random.randint(low = -100, high = 101, size = (1,3))

    ab = np.array(a-b)
    bc = np.array(b-c)
    ca = np.array(c-a)

    A = np.array(ab / bc)
    B = np.array(bc / ca)
    C = np.array(ca / ab)

    if np.all(A == A[0][0]):
        continue
    elif np.all(B == B[0][0]):
        continue
    elif np.all(C == C[0][0]):
        continue
    
    A_length = np.linalg.norm(ab)
    B_length = np.linalg.norm(bc)
    C_length = np.linalg.norm(ca)
    length = np.array([A_length, B_length, C_length])
    length = np.sort(length)

    if (length[2] < length[1] + length[0]):
        Hit = 1
        print(a,b,c)
        print("Goal! => Try : %d" %(Try))
    else:
        Try += 1


#2-1
arr1 = np.random.randint(low = 0, high = 11, size = (np.random.randint(low = 0, high = 11, size = None), np.random.randint(low = 0, high = 11, size = None)))
print(arr1)

arr2 = np.random.randint(low = 0, high = 11, size = (np.random.randint(low = 0, high = 11, size = None), np.random.randint(low = 0, high = 11, size = None)))
print(arr2)

#2-2
arr3 = arr1 + arr2
print(arr3)