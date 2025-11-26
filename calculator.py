class Calculator:
    def add(self, a, b):
        return a+b
    def subtract(self, a, b):
        return a-b
    def multiply(self, a, b):
        return a*b
    def divide(self, a, b):
        if b == 0:
            return "Denominator cannot be zero!"
        return a/b
        
    def menu(self):
        print()
        print("*"*50)
        print("CALCULATOR 🧮")
        print("*"*50)
        print("Press 1 for Addition ➕")
        print("Press 2 for Subtraction ➖")
        print("Press 3 for Multiplication ✖️")
        print("Press 4 for Division ➗")
        print("Press 5 To Exit Calculator 😊")
        print("*"*50)
        

    def run(self):
        while True:
            self.menu()
            try:
                choice = int(input("Choose a number from (1-5): "))
            except ValueError:
                print("Invalid Input! \nPlease Input Numbers Only \nThank You😊")
                continue
            if choice ==5:
                print("Thank You For Using Calculator😊 \nHave a Good Day👋")
                break
            if choice not in [1,2,3,4]:
                print("Invalid Number! \nPlease Enter Number Between (1-5) \nThank You😊")
                continue
            try:
                num1 = float(input("Enter a Number: "))
                num2 = float(input("Enter a Number: "))
            except ValueError:
                print("Please Enter Only Numbers 🙂" )
                continue
            if choice == 1:
                print()
                print(f"Addition Result ➕ : {num1}+{num2} = {self.add(num1,num2)}")
            elif choice == 2:
                print()
                print(f"Subtraction Result ➖ : {num1}-{num2} = {self.subtract(num1,num2)}")
            elif choice == 3:
                print()
                print(f"Multiplication Result ✖️ : {num1}*{num2} = {self.multiply(num1,num2)}")
            elif choice == 4:
                print()
                print(f"Division Result ➗ : {num1}/{num2} = {self.divide(num1,num2)}")

calc = Calculator()
calc.run()