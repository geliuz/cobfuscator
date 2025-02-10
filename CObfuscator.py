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
    
    import re

    def format_c_code(self, code):
        """Format C code with proper indentation and spacing."""
        # First, separate includes, macros, and code
        lines = code.split('\n')
        includes = []
        macros = []
        code_lines = []

        # Split combined includes and defines into separate lines
        for line in lines:
            parts = line.strip().split(' #')  # Split on macro/include boundaries
            for part in parts:
                if part:
                    if part.startswith('include'):
                        # Remove spaces between <>, remove leading spaces, and add carriage return after >
                        fixed_include = re.sub(r'\s*#?\s*include\s*<\s*([a-zA-Z0-9.]+)\s*>', r'#include<\1>\n', part)
                        includes.append(fixed_include.strip())
                    elif part.startswith('define'):
                        macros.append(f'#{part.strip()}')
                    else:
                        code_lines.append(part)

        # Format the main code
        indent_level = 0
        formatted_code = []

        for line in code_lines:
            stripped = line.strip()
            if not stripped:
                continue

            # Decrease indent for closing braces
            if stripped.startswith('}'):
                indent_level = max(0, indent_level - 1)

            # Add proper indentation
            formatted_code.append('    ' * indent_level + stripped)

            # Increase indent for opening braces
            if stripped.endswith('{'):
                indent_level += 1

            # Handle single-line if/else cases
            if stripped.endswith('}') and not stripped.startswith('}'):
                indent_level = max(0, indent_level - 1)

        # Combine all parts
        result = []

        # Add includes at the top, each on its own line
        if includes:
            result.extend(includes)

        # Add macros, each on its own line
        if macros:
            result.extend(macros)
            result.append('')  # Empty line after macros

        # Add formatted code
        result.extend(formatted_code)

        # Join everything and format operators
        final_code = '\n'.join(result)

        # Add space after commas
        final_code = re.sub(r',(?=\S)', ', ', final_code)

        # Add space around operators
        final_code = re.sub(r'\s*([=+\-*/<>])\s*', r' \1 ', final_code)

        # Fix includes to ensure no spaces between < and >, remove leading spaces, and add carriage return after >
        final_code = re.sub(r'#include\s*<\s*([^>\s]+)\s*>', r'#include<\1>\n', final_code)

        # Remove whitespace at the beginning of lines that start with #
        final_code = re.sub(r'^\s*(#)', r'\1', final_code, flags=re.MULTILINE)

        return final_code



        
    def obfuscate(self, code):
        """Apply all obfuscation techniques to the input code."""
        result = code
        result = self.obfuscate_variables(result)
        result = self.obfuscate_functions(result)
        result = self.add_junk_macros(result)
        result = self.split_lines(result)
        # Format the final code
        result = self.format_c_code(result)
        return result