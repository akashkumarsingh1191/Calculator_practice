from Utils.history import History_Manager
from operation import Operation
class Calculation:
    def __init__(self, num1, num2, symbol):
        self.number1 = num1
        self.number2 = num2
        self.symbol = symbol
        self.operation = Operation(self.number1, self.number2) #composition
        self.history = History_Manager() #compositon

    def cal_operation(self):
        if self.symbol == '+':
            self.result, self.status = self.operation.addition()
            self.history.record(self.number1,self.number2,self.symbol,self.result,self.status)
            return self.result
        elif self.symbol == "-":
            self.result, self.status  = self.operation.subtraction()
            self.history.record(self.number1,self.number2,self.symbol,self.result,self.status)
            return self.result
        elif self.symbol == "*":
            self.result, self.status  = self.operation.multiplication()
            self.history.record(self.number1,self.number2,self.symbol,self.result,self.status)
            return self.result
        elif self.symbol == "/":
            self.result, self.status  = self.operation.division()
            self.history.record(self.number1,self.number2,self.symbol,self.result,self.status)
            return self.result
        elif self.symbol == "%":
            self.result, self.status  = self.operation.reminder()
            self.history.record(self.number1,self.number2,self.symbol,self.result,self.status)
            return self.result
        else:
            return f"Return valid operator..."
    def clear_history(self):
        self.history.clear_history()
