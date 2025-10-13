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
        if not self.__records:
            print(f'History is not Available..')
        else:
            print(f'.....Calculation History.....\n')
            for i, record in enumerate(self.__records,start = 1):
                print(f"[{i}] {record['Number 1']} {record['Operator']} {record['Number 2']} = {record['Result']} {record['Status']}")
                # print(f"[{i}] {record['Number 1']} {record['Operator']} {record['Number 2']} = {record['Result']}" f"{{record['Status']} if record['Status'] else {record['Status']}}")
        # return self.__records
    
    def clear_history(self):
        self.__records.clear()
        return f'History is cleared..'

    