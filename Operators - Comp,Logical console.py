Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5+4j
>>> #complex no - real+imaginary(j)
>>> x.real
5.0
>>> x.imag
4.0
>>> type(x)
<class 'complex'>
>>> x = 1
>>> type(x)
<class 'int'>
>>> x = 45.45
>>> type(x)
<class 'float'>
>>> x = "Tanuj"
>>> type(x)
<class 'str'>
>>> 22/7
3.142857142857143
>>> 22//7
3
>>> #//-floor divison
>>> 5>10
False
>>> 10<500
True
>>> 10 = 10
SyntaxError: cannot assign to literal
>>> 10==10
True
>>> 10>=100
False
>>> 10>=10
True
>>> 10 != 5
True
>>> 10!=10
False
>>> 10>=5 and 10<=100
True
>>> 10 == 10 and 5>10
False
>>> 10==10000 or 5>1
True
>>> 10 == 10
True
>>> not(10==10)
False
>>> not(True)
False
>>> not(False)
True
>>> 