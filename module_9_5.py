class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        if self.step == 0:
            raise StepValueError
        elif self.step < 0:
            if self.pointer > self.stop and self.pointer + self.step > self.stop:
                self.pointer += self.step
            else:
                raise StopIteration
        elif self.step > 0:
            if self.pointer < self.stop and self.pointer + self.step < self.stop:
                self.pointer += self.step
            else:
                raise StopIteration
        else:
            raise StepValueError
        return self.pointer


iter1 = Iterator(100, 200, 0)
try:
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()