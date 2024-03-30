import os 
class FizzBuzz:
    def __init__(self , number:int):
        self.numbers = number
    def FizzBuzz(self):
        os.system('cls')
        print(f'FizzBuzz Game §')
        for i in range(self.numbers+1):
            if i%3 == 0 and i%5 == 0 :
                print(f"{i} - FizzBuzz")
            elif i%3 == 0 and i != 0:
                print(f"{i} - Fizz")
            elif i%5 == 0 and i != 0:
                print(f"{i} - Buzz")
            else :
                print(i)
 

game = FizzBuzz(number=int(input('Enter finish number : ')))
game.FizzBuzz()
