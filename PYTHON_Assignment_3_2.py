"""
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

"""

str1="ACADGILD"
output1=[str1[x] for x in range(len(str1))]
print (output1)	##['A', 'C', 'A', 'D', 'G', 'I', 'L', 'D']

str2=['x','y','z']
output2=[i*j for i in str2 for j in range(1,5)]
print (output2)	##['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

output3=[i*j for j in range(1,5) for i in str2]
print (output3)	##['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

output4=[[i+j] for i in range(2,5) for j in range(3)]
print (output4)	##[[2], [3], [4], [3], [4], [5], [4], [5], [6]]

lst=[i for i in range(2,6)]
output5=[[x+i for x in lst] for i in range(4)]
print (output5)	##[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]

output6=[(j,i) for i in range(1,4) for j in range(1,4)]
print (output6) ##[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]


