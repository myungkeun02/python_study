odd = [1,2,3,4]
print(odd)
print(type(odd))

print(f'{"리스트의 인덱싱":-^50}')

a = [1,2,3,]
print(a)
print(a[0])
print(a[1])
print(a[0] + a[1])
print(a[-1])

b = [1,2,3,['a','b','c']]
print(b[3][0])

print(f'{"리스트의 슬라이싱":-^50}')

a = [1,2,3,4,5]
b = a[:2]
print(b)

print(f'{"리스트 연산 하기":-^50}')
c = a + b
print(c)
print(c * 3)

print(f'{"리스트 길이 구하기":-^50}')
print(len(c))

print(f'{"리스트의 값 수정하기":-^50}')
a = [1,2,3]
a[2] = 5
print(a)

del a[0]
print(a)

print(f'{"리스트 관련 함수":-^50}')
a = [1,2,3]
a.append(4)
print(a)
a.append([5,6])
print(a)

b = [4,3,1,5,2]
b.sort()
print(b)
c = ['a','c',"b",'d','f','e']
c.sort()
print(c)
c.reverse()
print(c)
print(c.index('b'))
c.remove('e')
print(c)
c.insert(0, "e")
print(c)
c.pop() #리턴해준댔는데?
print(c)
c.pop(0) #리턴해준댔는데?
print(c)

a = [1,2,3]
a.extend([4,5,6])
print(a)

a+=[7,8]
print(a)