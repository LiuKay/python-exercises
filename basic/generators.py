'''
Generators in Python are a way to create iterators. An iterator is an object that can be iterated (looped) upon, meaning that you can traverse through all the values of an iterator, one by one.

A generator is a special type of iterator. It is defined using a function, but instead of using the return keyword to return a value, it uses the yield keyword to produce a value.
'''

def my_range(n):
    i = 0
    while i <n:
        yield i
        i+=1


# for i in my_range(5):
#     print(i)


def count_up_to(n):
    i =1
    while i<=n:
        yield i
        i+=1


counter = count_up_to(3)

print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter)) # error


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()
for i in range(10):
    print(next(f))



