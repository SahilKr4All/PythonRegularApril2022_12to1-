#How to store values in List and How to Print list values
x = []
store = True
while store == True:
    choice = int(input("Enter Value : "))
    x.append(choice)

    val = input("do you want to add more : Y/N=> ").lower()
    if val == "n":
        store = False
    
'''
for i in range(0,len(x)):
    print(x[i])
'''

for value in x:
    print(value)
