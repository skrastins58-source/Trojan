#!/usr/bin/env python3
"""
Example Python code to demonstrate Sourcery refactoring capabilities.
This file contains intentionally inefficient code patterns that Sourcery would improve.
"""

def process_items(items):
    """Process a list of items with inefficient patterns."""
    # Inefficient: using loop instead of list comprehension
    result = []
    for item in items:
        if item > 0:
            result.append(item * 2)
    return result

def find_first_match(data, target):
    """Find first matching item with inefficient pattern."""
    # Inefficient: using loop instead of next()
    for item in data:
        if item == target:
            return item
    return None

def check_conditions(value):
    """Check multiple conditions inefficiently."""
    # Inefficient: nested if statements
    if value is not None:
        if isinstance(value, int):
            if value > 0:
                return True
    return False

def format_names(names):
    """Format names inefficiently."""
    # Inefficient: manual string building
    formatted = ""
    for i, name in enumerate(names):
        if i == 0:
            formatted = name.title()
        else:
            formatted = formatted + ", " + name.title()
    return formatted

def get_config_value(config, key, default=""):
    """Get configuration value inefficiently."""
    # Inefficient: unnecessary intermediate variable
    if key in config:
        value = config[key]
        return value
    else:
        return default

# Example usage (would also be optimized by Sourcery)
if __name__ == "__main__":
    sample_data = [1, -2, 3, -4, 5]
    print("Original data:", sample_data)
    print("Processed:", process_items(sample_data))
    
    print("First positive:", find_first_match(sample_data, 3))
    print("Condition check:", check_conditions(5))
    
    names = ["alice", "bob", "charlie"]
    print("Formatted names:", format_names(names))
    
    config = {"debug": True, "port": 8080}
    print("Config value:", get_config_value(config, "debug", False))