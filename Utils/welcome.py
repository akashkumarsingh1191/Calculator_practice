class Welcome:
    
    @staticmethod
    def greet(name):
        return f'Welcome {name} for using this Application'
    
    @staticmethod
    def intro():
        return f'This Application perform several task i.e. **Addition**,**Subtraction**,**Multiplication**,**Division**'
    
print(Welcome.greet('Akash'))
print(Welcome.intro())