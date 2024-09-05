print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short"
print(len(a))
print("=" * 50)

c = "Life is too short, You need Python"
print(c[0]) #L
print(c[3]) #e
print(c[-1]) #n
print(c[0] + a[1] + a[2] + a[3]) #Life
print(c[0:4]) #Life a[시작_번호:끝_번호] -> 이때 끝 번호는 포함 시키지 않는다.
print(c[19:]) # You need Python
print(c[:17])
print("=" * 50)

num1 = 3
d = "Life is too short%s%d" % (", You need Python", num1)
print(d)

num2 = 98
print("%d%%" % num2)

print("%10s" % "hi")
print("%-10s" % "hi")

print("=" * 50)

print("%0.4f" % 3.141592)

print("=" * 50)

print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
a = 1
b = "four"
print("I eat {0} apples".format(a))
print("I eat {0} apples".format(b))
print("I eat {0} apples. so I was sick for {1} days".format(a, b))
print("I ate {number} apples. so I was sick for {day} days.".format(number=a, day=b))

print("=" * 50)

print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

print("=" * 50)

print(f'{"hi":=^50}')