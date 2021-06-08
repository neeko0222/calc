# imports go here i guess, apparently therees a math operations import! that would of beem helpful!!!

# test 1/2
print('code starts here')

#would  __add__ be better? I need to check up on different methods. is __init__ just the default?

# not working

# class Symbol_func:
#     def __init__(symbols):
#         symbols.list = ['+','-']
  
  #stuck here


        
    
#combine these two somehow

class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(add):
        return add.a + add.b  # tried just adding "+" in between here no error but it didnt work! :(
    def sub(sub):
        return sub.a - sub.b
        

    
    def display_minus(display):
        print(display.a ,"-", display.b)

    def display_plus(display): 
        print(display.a ,"+", display.b)  

# why do I not need to use int() here? what is the relationship between integer/strings within a class/function? so many questions!!!
# also when should i use print vs return. I know return changes the flow of the program, so would I use return here instead of print?




 
entry00 = Calculate(11, 10), 
entry01 = Calculate(55,5)






entry01.display_minus()
entry01.display_plus()

print('=', Calculate.sub(entry00))
print('=', Calculate.sub(entry01))








# test 2/2
print('code ends here')
