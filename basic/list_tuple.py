# -*- coding: utf-8 -*-

classmates = ['a', 'b', 'c']
print(classmates)

classmates.append('d')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

last = classmates.pop()
print(last)
print(classmates)

test_list = ["aaa", 111]
print(test_list)

# tuple: cannot modify after init
test_tuple = ("a", "b", "c")
print(test_tuple)

t = ()
print(t)

t1 = (1)  # => t1=1
print(t1)

t2 = (1,)
print(t2)

t3 = ('a', 'b', ['A', 'B'])
print(t3)
t3[2][0] = 'X'
t3[2][1] = 'Y'
print(t3)

