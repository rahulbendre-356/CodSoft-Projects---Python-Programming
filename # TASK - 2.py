from termcolor import colored
import time
import random

def display_ascii_art():
    art = """
    ┌─────────────────────────────────────┐
    │  ██████╗ █████╗ ██╗      ██████╗   │
    │ ██╔════╝██╔══██╗██║     ██╔════╝   │
    │ ██║     ███████║██║     ██║        │
    │ ██║     ██╔══██║██║     ██║        │
    │ ╚██████╗██║  ██║███████╗╚██████╗   │
    │  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝   │
    └─────────────────────────────────────┘
    """
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    print(colored(art, random.choice(colors)))

def typewriter_effect(text, color='white', delay=0.03):
    for char in text:
        print(colored(char, color), end='', flush=True)
        time.sleep(delay)
    print()

class MathProcessor:
    def __init__(self):
        self.equation = ""
        self.operands = []
        self.operator = ""
        
    def capture_input(self):
        typewriter_effect("╭─ Enter your calculation: ", 'cyan', 0.02)
        self.equation = input(colored("╰─➤ ", 'cyan'))
        
    def parse_expression(self):
        components = self.equation.strip().split()
        
        if len(components) != 3:
            raise ValueError("Format should be: number operator number")
            
        try:
            first_num = float(components[0])
            operation = components[1]
            second_num = float(components[2])
            
            self.operands = [first_num, second_num]
            self.operator = operation
            
        except ValueError:
            raise ValueError("Invalid numbers detected!")

class ArithmeticEngine:
    def __init__(self, operand_a, operand_b, operation_type):
        self.a = operand_a
        self.b = operand_b
        self.op = operation_type
        self.answer = None
        
    def execute_addition(self):
        return self.a + self.b
        
    def execute_subtraction(self):
        return self.a - self.b
        
    def execute_multiplication(self):
        return self.a * self.b
        
    def execute_division(self):
        if self.b == 0:
            return colored("⚠️  Division by zero detected!", "red")
        return self.a / self.b
        
    def compute(self):
        operations_map = {
            '+': self.execute_addition,
            '-': self.execute_subtraction,
            '*': self.execute_multiplication,
            'x': self.execute_multiplication,
            '×': self.execute_multiplication,
            '/': self.execute_division,
            '÷': self.execute_division
        }
        
        if self.op in operations_map:
            self.answer = operations_map[self.op]()
        else:
            self.answer = colored("❌ Unknown operation!", "red")
            
        return self.answer

def show_calculation_result(expression, result):
    print(colored("\n" + "─" * 40, 'blue'))
    typewriter_effect("📊 COMPUTATION COMPLETE", 'green', 0.05)
    print(colored("─" * 40, 'blue'))
    
    print(colored(f"Expression: {expression}", 'white'))
    print(colored(f"Answer: ", 'yellow'), end='')
    
    # Animate result display
    result_str = str(result)
    for char in result_str:
        print(colored(char, 'yellow'), end='', flush=True)
        time.sleep(0.1)
    print("\n" + colored("─" * 40, 'blue'))

def main_calculator_loop():
    session_count = 0
    
    while True:
        session_count += 1
        
        print(colored(f"\n{'═' * 45}", 'magenta'))
        print(colored(f"SESSION #{session_count:03d}", 'magenta'))
        print(colored(f"{'═' * 45}", 'magenta'))
        
        try:
            # Get user input
            processor = MathProcessor()
            processor.capture_input()
            
            # Parse and validate
            processor.parse_expression()
            
            # Display parsed components
            typewriter_effect("🔍 Analyzing expression...", 'blue', 0.02)
            print(colored(f"   First operand: {processor.operands[0]}", 'white'))
            print(colored(f"   Operator: {processor.operator}", 'white')) 
            print(colored(f"   Second operand: {processor.operands[1]}", 'white'))
            
            # Calculate result
            engine = ArithmeticEngine(
                processor.operands[0], 
                processor.operands[1], 
                processor.operator
            )
            
            result = engine.compute()
            
            # Display result with animation
            show_calculation_result(processor.equation, result)
            
        except ValueError as error:
            print(colored(f"\n❌ INPUT ERROR: {str(error)}", 'red'))
            
        except Exception as error:
            print(colored(f"\n💥 SYSTEM ERROR: {str(error)}", 'red'))
            
        finally:
            print(colored("\n" + "─" * 45, 'green'))
            continue_prompt = input(colored("Continue calculating? [Y/n]: ", 'green'))
            
            if continue_prompt.lower() in ['n', 'no', 'exit', 'quit']:
                typewriter_effect("🚀 Calculator shutting down...", 'yellow', 0.05)
                typewriter_effect("Thanks for calculating with us!", 'cyan', 0.05)
                break
            
            # Clear screen effect
            print("\n" * 3)

if __name__ == '__main__':
    display_ascii_art()
    typewriter_effect("Welcome to the Retro Terminal Calculator!", 'cyan', 0.03)
    typewriter_effect("Format: number operator number (e.g., 5 + 3)", 'white', 0.02)
    
    main_calculator_loop()