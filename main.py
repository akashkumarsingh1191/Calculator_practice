from Utils.history import History_Manager
from operation import Operation
class Calculation:
    def __init__(self, num1, num2, symbol):
        self.__number1 = num1
        self.__number2 = num2
        self.symbol = symbol
        self.__result = None
        self.operation = Operation(self.__number1, self.__number2) #composition
        self.history = History_Manager() #compositon

    def __execute_and_history(self, operation_method):
        try:
            self.__result, self.status = operation_method()
            self.history.record(self.__number1,self.__number2,self.symbol,self.__result,self.status)
        except Exception as e:
            self.__result = 0
            self.status = False
            self.history.record(self.__number1,self.__number2,self.symbol,self.__result,self.status)
        return self.__result

    def set_value(self, symbol, new_value):
        self.symbol = symbol
        try:
            self.__number1 = 0 if self.__result is None or math.isinf(self.__result) else self.__result
        except Exception as e:
            print(f'Not able to convert the previous result..')
        try:
            self.__number2 = float(new_value)
            self.operation.set_value(self.__number1, self.__number2)
            return True
        except Exception as e:
            print(f'Invalid Input,Second number is not updated')
            self.__number2 = 0
            self.operation.set_value(self.__number1, self.__number2)
            return False  
        
    def backspace(self):
        pass

    def cal_operation(self):
        if self.symbol == '+':
            # self.__execute_and_history()
            return self.__execute_and_history(self.operation.addition)
        elif self.symbol == "-":
            return self.__execute_and_history(self.operation.subtraction)
        elif self.symbol == "*":
            return self.__execute_and_history(self.operation.multiplication)
        elif self.symbol == "/":
            return self.__execute_and_history(self.operation.division)
        elif self.symbol == "%":
            return self.__execute_and_history(self.operation.reminder)
        else:
            return f"Return valid operator..."
    def clear_history(self):
        self.history.clear_history()
