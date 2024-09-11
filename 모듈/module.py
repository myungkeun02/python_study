# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일이다. 모듈은 다른 파있너 프로그램에서 불러와 사용할 수 있도록 만ㄷ느 파이썬 파일이라고도 할 수 있다.
# 다른 사람들이 이미 만들어 놓은 모듈을 사용할 수 있고 내가 만들어서 사용할 수도 있다.

# import mod1

from mod1 import add, sub
import mod2

print(add(1,2))
print(sub(1,2))

print(mod2.PI)

a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4))