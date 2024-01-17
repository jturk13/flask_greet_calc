def add(a, b):
    """Add two numbers."""
    return a + b

def sub(a, b):
    """Subtract b from a."""
    return a - b

def mult(a, b):
    """Multiply two numbers."""
    return a * b

def div(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
