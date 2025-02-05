#Datatypes
#complex 
cmp1=7+3j
cmp2=9-4j
print(cmp1+cmp2)
print(cmp1-cmp2)
print(cmp1*cmp2)
print(cmp1/cmp2)
print(cmp1**cmp2)

#boolean  
print(5>4)
print(9<2)
print(5>=1)
print(7<=10)
print(type(False))
print(int(True))
print(int(False))

#list  
list1=[2,4,6,8,0, 'True', 'string', [1,3,5,7]]
print(type(list1))
print(list1)
print(list1[5])
print(list1[10])
print(len(list1))
print(list1[-7])
print(list1[-12])

#slicing
print(list1[2:5])
print(list1[3:5:3])
print(list1[-7])
print(list1[-2: 9: -1])
print(list1[6][10])

#tuple  
tup1=(1,2,3,4, 'True', 'str', 0.8)
print(tup1[2:4])
print(tup1[1:3:5])
print(tup1[2:3:-1])
print(tup1[-5:-3])

#range
range(0,100)
print(list(range(0,80)))
print(list(range(60,0,-1)))
print(list(range(0,60,-1)))
print(list(range(60,0,-3)))