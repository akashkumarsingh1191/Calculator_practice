import math
class Operation:
    def __init__(self, num1, num2):
        try:
            self.first_number = float(num1)
            self.second_number = float(num2)
        except ValueError as e:
            print(f"Error: {e}.Setting number to 0")
            self.first_number = 0
            self.second_number = 0
        self.__result = 0
        self.records = []
        self.symbol = ''
    
    def addition(self):
        self.symbol = "+"
        self.__result = self.first_number + self.second_number
        # self.record()
        return self.__result,True
    
    def subtraction(self):
        self.symbol = "-"
        self.__result = self.first_number - self.second_number
        # self.record()
        return self.__result,True
    
    def multiplication(self):
        self.symbol = "*"
        self.__result = self.first_number * self.second_number
        # self.record()
        return self.__result,True
    
    def division(self):
        self.symbol = "/"
        try:
            self.__result = self.first_number / self.second_number
            # self.record()
            return self.__result,True
        except ZeroDivisionError:
            self.__result = math.inf
            # self.record(False)
            return self.__result,False

    def reminder(self):
        self.symbol = "%"
        try:
            self.__result = self.first_number % self.second_number
            # self.record()
            # return self.__result
        except ZeroDivisionError:
            self.__result = self.first_number
            # self.record(False)
        return self.__result,True
