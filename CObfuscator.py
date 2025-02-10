import re
import random
import string

class CObfuscator:
    def __init__(self):
        self.variable_map = {}
        self.function_map = {}
        self.macros = []
        
    def generate_random_name(self, length=8):
        """Generate confusing variable names that look similar."""
        chars = 'OoIlL1' + string.ascii_letters
        return '_' + ''.join(random.choice(chars) for _ in range(length))
    
    def obfuscate_variables(self, code):
        """Find and replace all variable declarations with obfuscated names."""
        pattern = r'\b(?:int|char|float|double|long)\s+([a-zA-Z_][a-zA-Z0-9_]*)'
        declarations = re.finditer(pattern, code)
        
        for match in declarations:
            var_name = match.group(1)
            # Skip the word 'main' in any context
            if var_name != 'main' and var_name not in self.variable_map:
                self.variable_map[var_name] = self.generate_random_name()
                
        # Replace all variable occurrences
        for original, obfuscated in self.variable_map.items():
            code = re.sub(r'\b' + original + r'\b', obfuscated, code)
            
        return code
    
    def obfuscate_functions(self, code):
        """Find and replace all function declarations with obfuscated names."""
        pattern = r'\b(?:void|int|char|float|double|long)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        functions = re.finditer(pattern, code)
        
        for match in functions:
            func_name = match.group(1)
            # Skip the word 'main' in any context
            if func_name != 'main' and func_name not in self.function_map:
                self.function_map[func_name] = self.generate_random_name()
                
        # Replace function names
        for original, obfuscated in self.function_map.items():
            code = re.sub(r'\b' + original + r'\b', obfuscated, code)
            
        return code
    
    def add_junk_macros(self, code):
        """Add confusing macros at the top of the code."""
        junk_macros = [
            '#define ' + self.generate_random_name() + '(x) ((x))',
            '#define ' + self.generate_random_name() + ' 1',
            '#define ' + self.generate_random_name() + '(x,y) ((x)+(y))'
        ]
        return '\n'.join(junk_macros) + '\n\n' + code
    
    def split_lines(self, code):
        """Randomly split lines to make code harder to read."""
        lines = code.split('\n')
        result = []
        for line in lines:
            if len(line.strip()) > 0 and ';' in line:
                parts = line.split(';')
                for part in parts[:-1]:
                    if part.strip():
                        result.append(part.strip() + ';')
            else:
                result.append(line)
        return '\n'.join(result)
    
    def obfuscate(self, code):
        """Apply all obfuscation techniques to the input code."""
        result = code
        result = self.obfuscate_variables(result)
        result = self.obfuscate_functions(result)
        result = self.add_junk_macros(result)
        result = self.split_lines(result)
        return result

def main():
    # Example C code
    c_code = """
    #include <stdio.h>
    #include <stdlib.h>
    
    int add(int a, int b) {
        int result = a + b;
        return result;
    }
    
    int main() {
        int x = 5;
        int y = 10;
        int sum = add(x, y);
        printf("%d", sum);
        return 0;
    }
    """
    
    # Create an instance of the obfuscator
    obfuscator = CObfuscator()
    
    # Obfuscate the code
    obfuscated_code = obfuscator.obfuscate(c_code)
    
    # Print results
    print("Original code:")
    print(c_code)
    print("\nObfuscated code:")
    print(obfuscated_code)

if __name__ == "__main__":
    main()