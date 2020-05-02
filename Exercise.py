#s = 'django'
#print(s[0])
#print(s[2])
#print(s[1:3])
#print(s[:4])
l = [1,2,[3,2,'hello']]
l[2][2] = 'goodbye'
print(l[2][2])

dic = {'k1':[{'nest_k':['this is deep',['hello']]}]}
print(dic['k1'][0]['nest_k'][1])

mylist =[1,1,1,1,1,2,2,2,3,3,3,3]
s = set(mylist)
print(s)

age = 24
name = 'Tanshed'
print("Hello, This is {name} and I am {age}".format(name = name, age = age))
