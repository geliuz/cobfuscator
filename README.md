# CObfuscator

CObfuscator is a powerful Python package that transforms readable C code into functionally equivalent but harder-to-understand code. Perfect for protecting intellectual property, making reverse engineering more challenging, or learning about code transformation techniques.

![PyPI version](https://img.shields.io/pypi/v/cobfuscator)
![Python versions](https://img.shields.io/pypi/pyversions/cobfuscator)
![License](https://img.shields.io/pypi/l/cobfuscator)

## Overview

CObfuscator takes your C source code and applies various transformations to make it more difficult to understand while preserving its original functionality. It's like having a translator that converts your clear, readable code into a mysterious yet functionally identical version.

Key Features:
- Transforms variable and function names into cryptic alternatives
- Adds misleading dead code and complex expressions
- Modifies control flow structures while maintaining logic
- Introduces confusing macros and string transformations
- Preserves code functionality while increasing complexity

### Installation & Use

```bash
pip install cobfuscator

### Basic Usage

```python
from cobfuscator import CObfuscator

# Create an obfuscator instance
obfuscator = CObfuscator()

# Your original C code
c_code = """
int add(int a, int b) {
    int result = a + b;
    return result;
}
"""

# Obfuscate the code
obfuscated_code = obfuscator.obfuscate(c_code)
```
