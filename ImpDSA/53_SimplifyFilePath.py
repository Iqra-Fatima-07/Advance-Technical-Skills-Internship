'''
Problem 53 :

Simplify a File Path

Topic: Stack, Strings

Problem Statement:

A file system path may contain:

/ representing a directory separator

. representing the current directory

.. representing the parent directory

directory names

Simplify the given absolute path and return its canonical form.

Multiple consecutive / characters should be treated as a single separator.

Input Format:

A single line containing an absolute path.

Output Format:

Print the simplified path.

Constraints:

1 ≤ |path| ≤ 10^5

Path starts with /.

Sample Input:

/home//user/../documents/./file

Sample Output:

/home/documents/file
'''

path = input().strip()

stack = []

for part in path.split('/'):
    if part == '' or part == '.':
        continue

    if part == '..':
        if stack:
            stack.pop()
    else:
        stack.append(part)

print('/' + '/'.join(stack))