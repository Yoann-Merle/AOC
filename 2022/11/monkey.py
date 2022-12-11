class Monkey:
    number = 0
    items= []
    items_inspected = 0

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


    def __init__(self, args: list, stress_reduction = True):
        self.sr = stress_reduction
        self.items = [int(x) for x in args[1].split(':')[1].split(',')]
        self.operation = self.parse_operation(args[2])
        self.divider = int(args[3].split()[-1:][0])
        self.monkey_true = int(args[4].split()[-1:][0])
        self.monkey_false = int(args[5].split()[-1:][0])

    def operate_and_throw(self):
        trown_items = []
        for item in self.items:
            self.items_inspected += 1
            if self.sr:
                new = int(self.operation(item) / 3)
            else:
                new = int(self.operation(item))
            trown_items.append(self.test(new))
        self.items = []
        return trown_items
