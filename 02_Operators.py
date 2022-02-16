# Let see an example, 2+7: Here "2" and "7" are Operands and "+" is an Operator.
    # Each operands and operators have their types.

# Based on Operands: There are two Operands viz. Unary and Binary Operator.
    # Unary means one. E.x : -5, +8,etc.
    # Binary means two. E.X : 5 + 8, 9 - 8,etc.

# Based on Operator: 
    # Arithmetic Operator:
            # Negation : -5
            # Addition : 5 + 7
            # Subraction : 6 - 5
            # Multiplication : 8 * 2
            # Division : 6 / 3
            # Truncating division or floor division : 5 // 4
            # Modulus : 6 % 7
            # Exponential : 3 ** 6
            
    # Relational Operator :
            # Equal : ==
            # Not Equal : !=
            # less than : <
            # Greater than : > 
            # Less than or Equal to : <=
            # Greater than or Equal to : >=

    # Membership Operator :
            # in 
            # not in 

    # Boolean Operator :
            # And
            # Or 
            # Not

    # Bitwise Operator :
            # & (And)
            # | (Or)
            # ^ (Xor)
            # ~ (Not)
            # << (Zero fill left)
            # >> (Signed fill right)
        
    # Identity Operator :
            # is
            # is not
        


a = 7 
b = 3

# Arithmetic Operator :--->

print("The addition of a and b is : ", a + b)  # Addition operator is "+"
print("The Subtraction of a and b is : ", a - b) # Subraction operator is "-"
print("The Multiplication of a and b is : ", a * b) # Multiplication operator is "*"
print("The Division of a and b is : ", a / b) # Division operator done by using "/"
print("The Truncating Division of a and b is :", a//b) # Truncating Division done by using "//" it will not print the decimal values
print("The Remainder of a and b is : ", a % b) # Remainder operator is "%"
print("The Exponential of a over b is : ", a**b) # Square operator is "**"

# Relational Operator:

print("a is greater than b ", a > b)
print("b is greater than a ", b > a)
print("a is greater or equal to a ", a >= b)
print("a is less or equal to b ", b <= a)
print("a is not equal to b", a != b)
print("a is equal to b ", a == b)

# Membership Operator:
c = [1,3,4,5,6,7,9,10]

print("5 present in c ", 5 in c) # Here 5 is present in list c so it's a case of "in"
print("2 is present in c", 2 in c) # Here 2 is not present in list c so it's a case of "Not in" 

# Boolean Operator: 

print("a is Greater than b and Equal to a using boolean operator :", a>b and a==7)
print("a is less than b and Not Equal to b using boolean operator :", a<b and a!=b)
print("a is less than b or equal to a using boolena operator :", a<b or a==7)
print("a is Greater than b or not equal to b using boolean operator", a>b or a!=b)
print("a is not greater than b :", a!=b)

# Bitwise Operator :



# Short-cirucit evaluation or lazy evaluation :
#   In this following example, "and" Operator the interpreter only check whether the first given value is "true" or not. If it's true then it will go for the next operator but in this case the first operator is false so the interpreter only checks the first one which is a "false" and will going to display "false" this is called "short-circuit evaluation" or "lazy evaluation". And similar for "or" too here only the change is if the first value is true then it will not check for other.

a1 = 2
b1 = 3
b2 = 3 
print("a1 is greater than b1 and b2 == b1 : ", a1>b1 & b1==b2 )

# Identity Operator:

a = 2
b = 2

print(a is b)
print(a is not b)