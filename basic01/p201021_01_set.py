#set(집합)
# s = {'a','b','a'}
# print(type(s))
# print(s)

s1 = {'a','b','c'}
s2 = {'b','c','d'}
print(s1 & s2)#교집합
print(s1 | s2)#합집합
print(s1 - s2)#차집합
print(s2 - s1)#차집합