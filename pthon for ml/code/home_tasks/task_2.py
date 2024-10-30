class Calculator:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        
        return a / b

    def calculator(self):
        """Main calculator logic to get user input and perform operations."""
        print("Welcome to the calculator!")
        print("Choose an operation:")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")

        choice = input("Enter the number of the operation you want to perform (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                return
            
            if choice == '1':
                print(f"{num1} + {num2} = {self.add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {self.subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {self.multiply(num1, num2)}")
            elif choice == '4':
                result = self.divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please select a valid operation (1/2/3/4).")

# Usage example
if __name__ == "__main__":
    calculator = Calculator()
    calculator.calculator()
