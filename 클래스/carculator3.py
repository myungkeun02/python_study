class Carculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Carculator()
cal2 = Carculator()

print(cal1.add(2))
print(cal2.add(2))
print(cal1.add(3))
print(cal2.add(3))
print(cal1.add(4))
print(cal2.add(4))
