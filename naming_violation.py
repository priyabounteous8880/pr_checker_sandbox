# naming_violation.py
# Modified `naming_violation.py` with **more intentional naming violations** for your AI Code Reviewer PR test

def CalculateSum(arr: list[int]) -> int:  # Violation: PascalCase function name
    totalSum = 0  # Violation: CamelCase variable name
    for i in arr:
        totalSum += i
    return totalSum

def GreetUser(Name: str) -> None:  # Violation: PascalCase function name, parameter should be snake_case
    print("Hello, " + Name)

# Additional intentional naming violations

def addNumbers(x, y):  # Violation: should be snake_case, parameters should have type hints
    return x + y

def Multiply_Numbers(a: int, b: int) -> int:  # Violation: PascalCase with underscore
    resultValue = a * b  # Violation: CamelCase variable name
    return resultValue

class personClass:  # Violation: class name should be PascalCase
    def __init__(self, Name, Age):  # Violation: parameters should be snake_case
        self.Name = Name  # Violation: attributes should be snake_case
        self.Age = Age

    def DisplayInfo(self):  # Violation: PascalCase method
        print(f"Name: {self.Name}, Age: {self.Age}")

CONSTANTvalue = 100  # Violation: constants should be UPPER_SNAKE_CASE

anotherConstant = 200  # Violation: constants should be UPPER_SNAKE_CASE

def processlist(ListOfItems):  # Violation: snake_case function name, parameter in PascalCase
    for Item in ListOfItems:  # Violation: PascalCase variable name
        print(Item)

