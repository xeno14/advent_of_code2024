def parse(s:str):
    import re
    parts = s.strip().split('\n\n')
    registers = list(map(int, re.findall(r'Register .: (\d+)', parts[0])))
    program = list(map(int, re.findall(r'([0-9])+', parts[1])))

    return registers, program


EXAMPLE1 = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

EXAMPLE2 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""


class Computer:

    def __init__(self, a:int, b:int, c:int, code:list[int]):
        self.a = a
        self.b = b
        self.c = c
        self.output = []
        self.code = list(code)
        self.pos = 0
    
    def dump(self):
        print(f'A={self.a} B={self.b} C={self.c} {self.output}')
        print('code=' + ''.join(map(str, self.code)))
        print('     ' + (' ' * self.pos) + '^^')
    
    def reset(self, a=0, b=0, c=0):
        self.pos = 0
        self.a = a
        self.b = b
        self.c = c
        self.output = []
    
    @property
    def opcode(self) -> int:
        return self.code[self.pos]
    
    @property
    def operand(self) -> int:
        return self.code[self.pos+1]
    
    @property
    def combo(self) -> int:
        match self.operand:
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case _:
                return self.operand

    def adv(self):
        self.a = self.a // (2 ** self.combo)
        self.pos += 2
    
    def bxl(self):
        self.b = self.b ^ self.operand
        self.pos += 2
    
    def bst(self):
        self.b = self.combo % 8
        self.pos += 2
    
    def jnz(self):
        if self.a == 0:
            self.pos += 2
            return
        self.pos = self.operand
    
    def bxc(self):
        self.b = self.b ^ self.c
        self.pos += 2
    
    def out(self):
        self.output.append(self.combo % 8)
        self.pos += 2
    
    def bdv(self):
        self.b = self.a // (2 ** self.combo)
        self.pos += 2
    
    def cdv(self):
        self.c = self.a // (2 ** self.combo)
        self.pos += 2

    def next(self):
        match self.opcode:
            case 0:
                self.adv()
            case 1:
                self.bxl()
            case 2:
                self.bst()
            case 3:
                self.jnz()
            case 4:
                self.bxc()
            case 5:
                self.out()
            case 6:
                self.bdv()
            case 7:
                self.cdv()
    
    def run(self):
        while self.pos < len(self.code):
            self.next()
            # self.dump()


def solve1(s: str):
    reg, prog = parse(s)
    c = Computer(a=reg[0], b=reg[1], c=reg[2], code=prog)
    c.run()
    return ','.join(map(str,c.output))


def solve2(s:str):
    _, program = parse(s)

    c = Computer(a=0, b=0, c=0, code=program)

    def rec(a, code):
        if len(code) == 0:
            return a

        last = code.pop()
        for r in range(8):
            c.reset(8*a+r)
            c.run()
            if c.output[0] == last and (ans := rec(8*a+r, code)) is not None:
                return ans
        code.append(last)
    
    return rec(0, list(program))


def main():
    # Computer(a=0, b=0, c=9, code=[2, 6]).run()
    # Computer(a=10, b=0, c=0, code=[5,0,5,1,5,4]).run()
    # Computer(a=2024, b=0, c=0, code=[0,1,5,4,3,0]).run()
    # Computer(a=0, b=29, c=0, code=[1,7]).run()
    # Computer(a=0, b=2024, c=43690, code=[4,0]).run()
    # Computer(a=729, b=0, c=0, code=[0,1,5,4,3,0]).run()
    # Computer(a=117440, b=0, c=0, code=[0,3,5,4,3,0]).run()

    assert solve1(EXAMPLE1) == '4,6,3,5,6,3,5,2,1,0'
    assert solve2(EXAMPLE2) == 117440

    with open('day17.txt') as f:
        my_input = f.read()
        print(solve1(my_input))
        print(solve2(my_input))


main()
