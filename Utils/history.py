class History_Manager:
    def __init__(self):
        self.__records = []
        
    def record(self,num1, num2, operator, result, status):
        self.__records.append(
            {
                "Number 1" : num1,
                "Operator" : operator,
                "Number 2" : num2,
                "Result" : result,
                "Status" : status
            }
        )
    def display_history(self):
        return self.__records
    
    def clear_history(self):
        self.__records.clear()
        return f'History is cleared..'
    
    