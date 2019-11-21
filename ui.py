import calc

class UserInterface:

    def __init__(self):
        self.arr = []

    def main(self):
        self.arr.append(self.askInput('operation'))
        self.arr.append(self.askInput('first'))
        self.arr.append(self.askInput('second'))
        self.promptUser()
        print('Answer: {}'.format( self.calculate() ))
        self.clearUserInput()

    def askInput(self, msg):
        if (msg == 'operation'):
            self.promptOperationsMenu()
        user_input = input('Give {} number: '.format(msg))
        return int(user_input)

    def calculate(self):
        result = "Something went wrong... check your input"
        if (self.arr[0] == 1):
            result = calc.add(self.arr[1], self.arr[2])
        elif (self.arr[0] == 2):
            result = calc.substract(self.arr[1], self.arr[2])
        elif (self.arr[0] == 3):
            result = calc.multiply(self.arr[1], self.arr[2])
        elif (self.arr[0] == 4):
            result = calc.divide(self.arr[1], self.arr[2])
        else:
            pass
        return result

    def promptUser(self):
        print('Your input was: operation#{} first#{} second#{}'
            .format(self.arr[0], self.arr[1], self.arr[2]))

    def promptOperationsMenu(self):
        print('Addition == 1')
        print('Substraction == 2')
        print('Multiplication == 3')
        print('Division == 4')

    def clearUserInput(self):
        self.arr.clear()

if __name__ == '__main__':
    calculation_ui = UserInterface()
    calculation_ui.main()