# naming_violation.py

def CalculateSum(arr: list[int]) -> int:
    totalSum = 0
    for i in arr:
        totalSum += i
    return totalSum

def GreetUser(Name: str) -> None:
    print("Hello, " + Name)

def addNumbers(X, Y):  # Missing type hints, PascalCase parameters
    return X + Y

def Multiply_Numbers(Age, Salary):  # PascalCase with underscore, PascalCase parameters
    resultValue = Age * Salary  # CamelCase variable
    return resultValue

class personClass:  # lowercase start class name
    def __init__(self, FirstName, LastName):  # PascalCase parameters
        self.FirstName = FirstName  # PascalCase attribute
        self.LastName = LastName

    def DisplayInfo(self):  # PascalCase method
        print(f"{self.FirstName} {self.LastName}")

CONSTANTvalue = 100  # Mixed case constant
AnotherConstant = 200  # Mixed case constant

def processlist(ListOfItems):  # PascalCase parameter
    for Item in ListOfItems:  # PascalCase loop variable
        print(Item)

def ComputeTotalSum(Values):  # PascalCase function, parameter
    totalsumValue = 0  # CamelCase
    for Val in Values:  # PascalCase
        totalsumValue += Val
    return totalsumValue

def HELPERFunction():  # All caps with Function suffix
    print("This is a helper function")

class utility_class:  # snake_case with class
    def DoWork(self):  # PascalCase
        print("Doing work")