from exercice.calculator_with_config.config import Config


class Calculator:
    def __init__(self, config: Config):
        self.prompt = config.get_prompt()
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def evaluate(self, a, b, op):
        if op == "add":
            return self.add(a, b)
        elif op == "subtract":
            return self.subtract(a, b)
        elif op == "multiply":
            return self.multiply(a, b)
        elif op == "divide":
            return self.divide(a, b)
        else:
            raise ValueError("Invalid operation.")

    def evaluate_quit(self, input_str):
        if input_str.lower() == 'q':
            print("Quitting calculator.")
            exit(0)

    def run_console(self):
        print("Simple Calculator,  enter 'q' to quit at anytime")
        a_input = input(f"{self.prompt} Enter value for a:").strip()
        self.evaluate_quit(a_input)
        b_input = input(f"{self.prompt} Enter value for b:").strip()
        self.evaluate_quit(b_input)
        try:
            a = float(a_input)
            b = float(b_input)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

        print("Select operation: add, subtract, multiply, divide")
        op = input("Operation: ").strip().lower()
        self.evaluate_quit(op)
        try:
            result = self.evaluate(a, b, op)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    calc = Calculator(config=Config())
    while True:
        calc.run_console()
