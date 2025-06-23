class Calculator:
    def Addition(self, a, b):
        return a + b
    
    def Subtraction(self, a, b):
        return a - b
    
    def Multiplication(self, a, b):
        return a * b
    
    def Division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero!"
    
    def Power(self, a, b):
        return a ** b

def main():
    cal = Calculator()
    while True:
        print("=" * 50)
        print("CALCULATOR APP")
        print("=" * 50)
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Exit")
        print("=" * 50)
        
        try:
            choice = int(input("Enter your choice (1/2/3/4/5/6): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1-6.")
            continue
        
        if choice not in range(1,7):
            print("Invalid choice! Please enter a number between 1-6.")
            continue
            
        if choice == 6:
            print("Thank you for using the calculator system!")
            break
        
        try:
            a = float(input("Enter the first value: "))
            b = float(input("Enter the second value: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.Don't enter Alphabets")
            continue
        
        if choice == 1:
            result = cal.Addition(a, b)
            print(f"Result: {a} + {b} = {result}")
        elif choice == 2:
            result = cal.Subtraction(a, b)
            print(f"Result: {a} - {b} = {result}")
        elif choice == 3:
            result = cal.Multiplication(a, b)
            print(f"Result: {a} × {b} = {result}")
        elif choice == 4:
            result = cal.Division(a, b)
            print(f"Result: {a} ÷ {b} = {result}")
        elif choice == 5:
            result = cal.Power(a, b)
            print(f"Result: {a} ^ {b} = {result}")
        
main()