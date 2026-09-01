'''
Problem 30 — Evaluate Reverse Polish Notation

Topic: Stack

Problem Statement

An arithmetic expression is written in Reverse Polish Notation (RPN). In RPN, an operator appears after its operands.

The expression contains integers and the operators +, -, *, and /. Division must truncate toward zero.

Evaluate the expression and return its integer result.

Input Format

The first line contains N, the number of tokens.

The second line contains N space-separated tokens.

Every operator has exactly two preceding valid operands.

Output Format

Print the resulting integer.

Constraints

1 ≤ N ≤ 2 × 10^5

Every intermediate result fits in signed 64-bit integer.

Division by zero never occurs.

Sample Input

5
2 3 + 4 *

Sample Output

20

Sample Explanation

The expression represents:

(2 + 3) × 4 = 20
'''

n = int(input())
tokens = input().split()

stack = []

for token in tokens:
    if token not in "+-*/":
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()

        if token == '+':
            stack.append(a + b)
        elif token == '-':
            stack.append(a - b)
        elif token == '*':
            stack.append(a * b)
        else:
            # Truncate division toward zero
            result = abs(a) // abs(b)

            if (a < 0) != (b < 0):
                result = -result

            stack.append(result)

print(stack[-1])