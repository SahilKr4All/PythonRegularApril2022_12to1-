'''
Loop - repetition - for , while
here in for-loop ,if start<end ending range is n-1
'''
'''
for i in range(1,11,2):
    print(i)

'''
# if end < start , end = n+1
'''
for i in range(10,0,-1):
    print(i)

'''
'''
for i in reversed(range(1,11)):
    print(i)

'''
'''
for i in range(2,21):
    print(i)
'''

'''
for i in reversed(range(2,21)):
    print(i)
'''
'''
for i in range(100,1000):
    print(i)
'''
'''
for i in range(1,11):
    print(f"2*{i}= {2*i}")
'''

'''
 result=0
 for i in range(1,11):
     result= result+i
# print(result)

# sum= 0
# for i in range(10,21):
#     sum= sum+i
# print(sum)

# sum= 0
# for i in range(1,11):
#     sum= sum-i
# print(sum)
'''
'''
*
**
***
****
*****
'''
'''
for i in range(1,6):
    print("*"*i)
'''

'''
    *
   **
  ***
 ****
*****
'''

# for i in range(1,6):
#     print(" "*(5-i)+"*"*i)

# break ,continue ,pass
# for i in range(1,10000000000001):
#     print(i)
#     if i==10:
#         break


# for i in range(1,11):
#     if (i%2==0):
#         continue

#     print(i)
'''
for i in range(1,2323):
    pass
'''
# for i in range( 50,100):
#     print(i)
#     if i==99:
#         break

#nested Loop=>
# 1
# 22
# 333
# 4444
# 55555
'''
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print(end="\n")
'''

# 1
# 12
# 123
# 1234
# 12345
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print(end="\n")