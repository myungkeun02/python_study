dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a = {1: 'h1'}
b = {'a': [1,2,3]}
print(dic)

print(f'{"딕셔너리 쌍 추가하기":=^50}')

a2 = {1: 'a'}
a2[2] = 'b'
print(a2)

a2['name'] = 'pey'
print(a2)

print(f'{"딕셔너리 요소 삭제하기":=^50}')

del a2[1]
print(a2)

grade = {'pey': 1, 'juliet': 99}
print(grade['pey'])
print(grade['juliet'])


#딕셔너리에서 key는 고유한 값이므로 중복되는 key 설정은 불가하다
#추가로 딕셔너리의 key 값으로 list는 올수없다 그 이유는 변화가 가능한 값이기 때문이다.


print(f'{'딕셔너리 관련 함수':=^50}')

dictionary = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

print(dictionary.keys())

for k in dictionary.keys():
    print(k)

dic_list = list(dictionary.keys())
print(dic_list)
dic_values = list(dictionary.values())
print(dic_values)

print(dictionary.items())

boolean1 = "name" in dictionary
print(boolean1)
boolean2 = "password" in dictionary
print(boolean2)