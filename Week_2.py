# 실습문제

# 0 
import numpy as np

# 1
a = np.arange(216).reshape(6,6,6)
print(a)

# 1-1
b = a[:, -1, ::2].flatten()
print(b)

# 1-2
c = a[a % 12 == 0]
print(c)

# 1-3
d = b - c
print(d)


# 2
x = np.arange(101)

# 2-1
is_prime = np.ones((101,) , dtype = bool)
is_prime[:2] = False

for i in range(101):
    if is_prime[i]:
        is_prime[i*i:101:i] = False

y = x[is_prime]
print(y)




# 이론문제

# 1 O
# 2 X
# 3 X
# 4 O
# 5 X
# 6 X