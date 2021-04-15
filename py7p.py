'''Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for x in range(1,5):
	print(x*'B')

	
B
BB
BBB
BBBB
>>> for x in range(5):
	print(x)

	
0
1
2
3
4
>>> for x in range(5):
	print(x,end='')

	
01234
>>> for x in range(5,1,-1):
	print(x*'B')

	
BBBBB
BBBB
BBB
BB
>>> for x in range(4,0,-1):
	print(x*'B')

	
BBBB
BBB
BB
B
>>> for x in range(5):
	print((5-x)*" "+'B'*x)

	
     
    B
   BB
  BBB
 BBBB
>>> for x in range(4,0,-1):
	print((x*" ")+'B'*x)

	
    BBBB
   BBB
  BB
 B
>>> for x in range(4):
	print((x*" ")+(4-x)*'B')

	
BBBB
 BBB
  BB
   B
>>> for x in range(4):
	print(x*'0'+'1'+(4-x)*'0')

	
10000
01000
00100
00010
>>> for x in range(3):
	print(x*'0')

	

0
00
>>> for x in range(4):
	print(x*'0'+(4-x)*'1')

	
1111
0111
0011
0001
>>> for x in range(4)
SyntaxError: invalid syntax
>>> for x in range(4):
	print((x*'1')+(4-x)*'0')

	
0000
1000
1100
1110
>>> for x in range(0,4):
	print((x*'1')+(4-x)*'0')

	
0000
1000
1100
1110
>>> for x in range(1,5):
	print((x*'1')+(4-x)*'0')

	
1000
1100
1110
1111
>>> for x in range(1,5):
	print(x+(x*'B'))

	
Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    print(x+(x*'B'))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for x in range(1,5):
	print((x)+(x*'B'))

	
Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    print((x)+(x*'B'))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for x in range(1,5):
	print(x*(x*'B'))

	
B
BBBB
BBBBBBBBB
BBBBBBBBBBBBBBBB
>>> for x in range(1,5):
	print(x+x*'B')

	
Traceback (most recent call last):
  File "<pyshell#55>", line 2, in <module>
    print(x+x*'B')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for x in range(4):
	print((x*" ")+(x*'B'))

	

 B
  BB
   BBB
>>> for x in range(4):
	print('x'+(x*'B'))

	
x
xB
xBB
xBBB
>>> for x in range(4):
	print((x-0)+(x*'B'))

	
Traceback (most recent call last):
  File "<pyshell#64>", line 2, in <module>
    print((x-0)+(x*'B'))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for x in range(4):
	print(x)

	
0
1
2
3
>>> for x in range(4):
	print(x++)
	
SyntaxError: invalid syntax
>>> 
>>> for x in range(4):
	print(x=x+1)

	
Traceback (most recent call last):
  File "<pyshell#71>", line 2, in <module>
    print(x=x+1)
TypeError: 'x' is an invalid keyword argument for print()
>>> for x in range(1,5):
	print(x)

	
1
2
3
4
>>> for x in range(1,5):
	print(x(x*'B'))

	
Traceback (most recent call last):
  File "<pyshell#75>", line 2, in <module>
    print(x(x*'B'))
TypeError: 'int' object is not callable
>>> for x in range(1,5):
	print((x*(x))+(x*'B'))

	
Traceback (most recent call last):
  File "<pyshell#77>", line 2, in <module>
    print((x*(x))+(x*'B'))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> type(x)
<class 'int'>
>>> '''

#Practice enumerates

'''for x,y in enumerate(['Hii','Hello','Great','Best']):
    	print(x,y)'''

'''for x,y in enumerate(('You','are','good','boy')):
    	#print(x,end='')
		#print(type(('You','are','good','boy')))
		print(y,end=' ')'''

#Using zip

'''Q=['Name','colour','shape']
A=['Orange','yellow','a circle']
for Q,A in zip(Q,A):
    	print('What is your {0}, I am {1}'.format(Q,A))'''






		





