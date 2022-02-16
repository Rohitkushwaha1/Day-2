# There are many different types of Data types. 
# This Data types are used to store data of different types in varaiables

a = "Rohit" # String Data type
b = 7.8 # float Data type
c = 5  # Integer Data type 
d = True # Boolean Data type
d2 = False #Boolean data type
e = () # Tuple Data type
f = {} # Dictionary Data type
g = {0} # Set Data type
i = [] # List Data type
j = 2 + 4j # complex Data type. For complex strictly use j as an imaginary number.
k = range(6)
l = frozenset({"android","MAC"})
m = b"Hello"
n = bytearray(5)
o = memoryview(bytes(1))

#python do not contain character data type


# To get the data type of any Variable just type(var_name)

print("The data type of a is : ",type(a))
print("The data type of b is : ",type(b))
print("The data type of c is : ",type(c))
print("The data type of d is : ",type(d))
print("The data type of d is : ",type(d2))
print("The data type of e is : ",type(e))
print("The data type of f is : ",type(f))
print("The data type of g is : ",type(g))
print("The data type of i is : ",type(i))
print("The data type of i is : ",type(j))
print("The data type of i is : ",type(k))
print("The data type of i is : ",type(l))
print("The data type of i is : ",type(m))
print("The data type of i is : ",type(n))
print("The data type of i is : ",type(o))

# you can even set the data type of the variable by using 

A = str("hello")
print(A)
B = int(9)
print(B)
C = float(20.5)
print(C)
D = complex(1+8j)
print(D)
E = list(('hey','hello'))
print(E)
F = tuple(("hey","hello"))
print(F)
G = range(7)
print(G)
H = dict(name="Rohit", age = "18")
print(H)
I = set(("hey","hello"))
print(I)
J = frozenset(("hey","hello"))
print(J)
K = bool(5)
print(K)
L = bytes(5)
print(L)
M = bytearray(5)
print(M)
N = memoryview(bytes(5))
print(N)

