# imports go here i guess

# test 1/2
print('code starts here')

#would  __add__ be better? I need to check up on diffrent ones. is __init__ just the default?

class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(add):
        return add.a + add.b
    def sub(sub):
        return sub.a - sub.b

# is there a cleaner way to do this? and why do I not need to use int() here? what is the relationship between integer/strings within a class/function? so many questions!!!
# also when should i use print vs return. I know return changes the flow of the program, so would I use return here instead of print?

    # def displayfunc(display):
    #     print(display.a ,"+", display.b)
 
entry00 = Calculate(10, 10)
entry01 = Calculate(5,5)

entry01.add() 

entry00.sub()

# entry01.displayfunc()
print('=', Calculate.add(entry01))
print('=', Calculate.sub(entry00))





# I want to fit all the operations into this list but right now I will focus on addition, i would normally try using functions but I read about Classes so today so I want to try and implement that here and if I get stuck mayb u can help
operations = []
pass

# test 2/2
print('code ends here')