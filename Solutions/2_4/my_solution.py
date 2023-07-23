

class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        return format(self.value, fmt)

    def __add__(self, other):
        if isinstance(other, int):
            return MutInt(self.value + other)
        elif isinstance(other, float):
            return MutInt(self.value + int(other))
        elif isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        else:
            raise NotImplementedError(f"Cannot add other {type(other)} to MutInt")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.value += other
        elif isinstance(other, float):
            self.value += int(other)
        elif isinstance(other, MutInt):
            self.value += other.value
        else:
            raise NotImplementedError(f"Cannot add other {type(other)} to MutInt")
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)

    __index__ = __int__
    __radd__ = __add__

def run():
    foo = MutInt(1)
    print(foo)
    print(f"{foo + 3} added int 3")
    print(f"{foo + 3.5} added float 3.5")
    print(f"{foo + MutInt(3)} added MutInt(3)")
    print(f"{3 + foo} added MutInt(3) to 3")
    print(f"converting MutInt(2) to int {int(MutInt(2))}")
    print(f"converting MutInt(2) to float {float(MutInt(2))}")

run()

if __name__ == "__main__":
    run()
