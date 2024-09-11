def add(a,b):
    return a+b

def sub(a,b):
    return a-b

# 이 구문은 mod1.py 파일을 직접 실행 했을떄는 아래 구문이 실행되고 외부에서 import 하여 사용하는 경우에는 if 문이 거짓이 되어 아래 구문을 실행하지 않는다.

# __name__ 변수는 파이썬이 내부적으로 사용하는 특별 이름 변수이다. 만약 mod1.py를 직접 실행하는 경우 해당 파일이 main 이기에 __main__이 저장되고,
# 다른 파일에서 import 할 경우 import를 하는 파일이 main이기에 import 당하는? mod1.py 의 __name__은 mod1 으로 저장된다.
if __name__ == '__main__':
    print(add(1,2))
    print(sub(1,2))