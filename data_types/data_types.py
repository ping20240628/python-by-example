
# Data Types
# Number, String, Bool, List, Tuple, Set, Dictionary

# Immutably: Number, String, Tuple

# Mutably: List, Dictionary, Set

# Number: int, float, bool, complex

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

a = 111
print(isinstance(a, int))

print(issubclass(bool, int))

print(True == 1)

print(False == 0)

print(True+1)
print(False + 1)

print(1 is True)
print(0 is False)

str = 'Runoob'

print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "TEST")

print('Ru\noob')

word = 'Python'
print(word[0], word[5])

print(word[-1], word[-6])

a = True
b = False
print(type(a))
print(type(b))

print(int(True))
print(int(False))

print(bool(0))
print(bool(42))
print(bool(''))
print(bool('Python'))
print(bool([]))
print(bool([1,2,3]))

print(True and False)
print(True and False)
print(not True)

print(5 > 3)
print(2 == 2)
print(7 < 4)

if True:
    print("This will always print")

if not False:
    print("This will also always print")

x = 10
if x:
    print("x is non-zero and thus True in a boolean context")
