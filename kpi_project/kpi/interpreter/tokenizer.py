# tokenizer.py
import re

def tokenize(expression):
    # Updated regex to capture numbers, words, operators, parentheses, and quoted strings
    tokens = re.findall(r'\s*(=>|<=|==|!=|[()\^*/+\-]|\d+\.\d+|\d+|[a-zA-Z_]\w*)\s*', expression)
    return tokens
