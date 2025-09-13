# Example Code Files

This directory contains example code files that demonstrate Sourcery's refactoring capabilities:

## Files

- **`demo_code.py`** - Python example with inefficient patterns that Sourcery would optimize
- **`demo_code.js`** - JavaScript example showing optimization opportunities

## Sourcery Improvements

When Sourcery analyzes these files, it would suggest improvements like:

### Python (`demo_code.py`)
- Convert manual loops to list comprehensions
- Use `next()` instead of manual iteration
- Simplify nested conditionals
- Use `join()` for string concatenation
- Remove unnecessary intermediate variables

### JavaScript (`demo_code.js`) 
- Use `filter()` and `map()` instead of manual loops
- Use `find()` method for array searching
- Simplify boolean logic
- Use `URLSearchParams` for URL building

## Running Examples

```bash
# Run Python example
python3 examples/demo_code.py

# Run JavaScript example (requires Node.js)
node examples/demo_code.js
```

## Testing with Sourcery

Once Sourcery is configured with a token:

```bash
# Analyze specific files
sourcery review examples/demo_code.py
sourcery review examples/demo_code.js

# Get refactoring suggestions
sourcery review --diff examples/
```

These examples demonstrate the type of improvements Sourcery provides for real codebases.