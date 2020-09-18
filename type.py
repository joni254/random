a = 2
b=7.99999


print('Hello, the id of the integer is {}'.format (id(b)))
print('Hello, the id of the integer is {}'.format (type(b)))
print('Hello, the id of the integer is {}'.format (TypeError(b)))

class DocOutput():
    '''Alaar!!'''

i = DocOutput()
print(DocOutput.__doc__)
print(type(i))
print(i)