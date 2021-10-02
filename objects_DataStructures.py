#1
print((60+(10 ** 2)/4*7)-134.75)
#2
print(4*(6+5))
print(4*6+5)
print(4+6*5)
#3
numbers = 3+1.5+4
print(numbers)
print(type(numbers))
#4
print(1 ** 0.5) #square root
print(100 ** 2) #square
#5
s = 'hello'
print(s[1])
print(s[-4])
print(s[4])
print(s[-1])
#6
my_list = [0,0,0]
print(my_list)
print([0]*3)
#7
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)
list4 = [5,3,4,6,1]
list4.sort()
sort_list4 = list4
print(list4)
#8
d = {'simple_key':'hello'}
print(d['simple_key'])
dd = {'k1':{'k2':'hello'}}
print(dd['k1']['k2'])
ddd = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(ddd['k1'][0]['nest_key'][1][0])
dddd = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(dddd['k1'][2]['k2'][1]['tough'][2][0])
#9
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))
#10
print(2 > 3)
print(3 <= 2)
print(3 == 2.0)
print(3.0 == 3)
print(4**0.5 != 2)
#11
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1'])




