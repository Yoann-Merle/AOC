class Monkey:
    def add_item(self, item):
        self.items.append(item)

    def parse_operation(self, instructions):
        def add(old):
            return old + operation_param
        def factor(old):
            return old * operation_param
        def square(old):
            return old * old

        _, ope, sec_arg = instructions.split('=')[1].split()
        if sec_arg == 'old':
            return square
        operation_param = int(sec_arg)
        if ope == '*':
            return factor
        else:
            return add

    def test(self, result):
        if result % self.divider == 0:
            return (self.monkey_true, result)
        return (self.monkey_false, result)


    def __init__(self, args: list):
        self.items_inspected = 0
        self.items = [int(x) for x in args[1].split(':')[1].split(',')]
        self.operation = self.parse_operation(args[2])
        self.divider = int(args[3].split()[-1:][0])
        self.monkey_true = int(args[4].split()[-1:][0])
        self.monkey_false = int(args[5].split()[-1:][0])

    def operate_and_throw(self):
        trown_items = []
        for item in self.items:
            self.items_inspected += 1
            new = int(self.operation(item) / 3)
            trown_items.append(self.test(new))
        self.items = []
        return trown_items

class ModuloMonkey:
    prime_dividers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27]

    def generate_item(self, item):
        new_item = {}
        for prime_divider in self.prime_dividers:
            new_item[prime_divider] = item % prime_divider
        return new_item

    def add_item(self, item):
        self.items.append(item)

    def parse_operation(self, instructions):
        def add(old):
            return old + operation_param
        def factor(old):
            return old * operation_param
        def square(old):
            return old * old

        _, ope, sec_arg = instructions.split('=')[1].split()
        if sec_arg == 'old':
            return square
        operation_param = int(sec_arg)
        if ope == '*':
            return factor
        else:
            return add

    def test(self, result):
        if result[self.divider] == 0:
            return (self.monkey_true, result)
        return (self.monkey_false, result)


    def __init__(self, args: list):
        self.items_inspected = 0
        self.items = []
        for it in args[1].split(':')[1].split(','):
            self.items.append(self.generate_item(int(it)))
        self.operation = self.parse_operation(args[2])
        self.divider = int(args[3].split()[-1:][0])
        self.monkey_true = int(args[4].split()[-1:][0])
        self.monkey_false = int(args[5].split()[-1:][0])

    def operate_and_throw(self):
        trown_items = []
        for item in self.items:
            self.items_inspected += 1
            new = {}
            for modulo in item:
                new[modulo] = int(self.operation(item[modulo])) % modulo
            trown_items.append(self.test(new))
        self.items = []
        return trown_items
