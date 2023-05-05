
# -*- coding: utf-8 -*-

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Age:%s. Gender:%s' % (25, True))

print('Hello, {0}'.format('kay'))

name = 'kay'
print(f'The name is {name}')

# encoding

print('中文'.encode('GB2312'))
print(b'\xd6\xd0\xce\xc4'.decode('GB2312'))