import math

class Operation:
    def __init__(self, num1, num2):
        try:
            self.__first_number = float(num1)
            self.__second_number = float(num2)
        except ValueError as e:
            print(f"Error: {e}.Setting number to 0")
            self.__first_number = 0
            self.__second_number = 0
        self.__result = 0
        self.records = []
        self.history = History_Manager()
        # self.symbol = ''
    
    def set_value(self,new_value):
        try:
            self.__first_number = 0 if math.isinf(self.__result) else self.__result
        except Exception as e:
            print(f'Not able to convert the previous result..')
        try:
            self.__second_number = float(new_value)
            return True
        except Exception as e:
            print(f'Invalid Input,Second number is not updated')
            self.__second_number = 0
            return False
    
    def reset_value(self):
        self.__first_number = 0
        self.__second_number = 0
        self.__result = 0
        self.history.clear_history()
        return f'Result as well as History reset..'
    
    def addition(self):
        # self.symbol = "+"
        self.__result = self.__first_number + self.__second_number
        return self.__result,True
    
    def subtraction(self):
        # self.symbol = "-"
        self.__result = self.__first_number - self.__second_number
        return self.__result,True
    
    def multiplication(self):
        # self.symbol = "*"
        self.__result = self.__first_number * self.__second_number
        return self.__result,True
    
    def division(self):
        # self.symbol = "/"
        try:
            self.__result = self.__first_number / self.__second_number
            return self.__result,True
        except ZeroDivisionError:
            self.__result = math.inf
            return self.__result,False

    def reminder(self):
        # self.symbol = "%"
        try:
            self.__result = self.__first_number % self.__second_number
            return self.__result, True
        except ZeroDivisionError:
            self.__result = math.inf
            return self.__result,False