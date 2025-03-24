https://infosecwriteups.com/creating-a-code-obfuscation-program-for-c-d10d604178d4

# CObfuscator

CObfuscator is a powerful Python package that transforms readable C code into functionally equivalent but harder-to-understand code. Perfect for protecting intellectual property, making reverse engineering more challenging, or learning about code transformation techniques.

## Overview

CObfuscator takes your C source code and applies various transformations to make it more difficult to understand while preserving its original functionality. It's like having a translator that converts your clear, readable code into a mysterious yet functionally identical version.

Key Features:
- Transforms variable and function names into cryptic alternatives
- Adds misleading dead code and complex expressions
- Modifies control flow structures while maintaining logic
- Introduces confusing macros and string transformations
- Preserves code functionality while increasing complexity

### Installation & Use

### Basic Usage

```python

# Create an obfuscator instance
obfuscator = CObfuscator()

# Your original C code
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
        int x = 6;
        int y = 11;
        int sum = add(x, y);
        printf("Hello World %d", sum);
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
```
