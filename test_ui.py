from ui import UserInterface
import unittest

class TestUI(unittest.TestCase):
    
    # TODO: Make better tests
    def test_ui(self):
        ui = UserInterface()
        ui.arr.append(1) 
        ui.arr.append(10) 
        ui.arr.append(20) 
        self.assertEqual(ui.calculate(), 30) # 10 + 20 = 30
        ui.clearUserInput()
        ui.arr.append(2) 
        ui.arr.append(11) 
        ui.arr.append(20)
        self.assertEqual(ui.calculate(), -9) # 10 - 20 = -9
        ui.clearUserInput()
        ui.arr.append(3) 
        ui.arr.append(10) 
        ui.arr.append(20)
        self.assertEqual(ui.calculate(), 200) # 10 * 20 = 200
        ui.clearUserInput()
        ui.arr.append(4) 
        ui.arr.append(10) 
        ui.arr.append(20)
        self.assertEqual(ui.calculate(), 0.5) # 10 / 20 = 0.5
        ui.clearUserInput()

if __name__ == '__main__':
     unittest.main()