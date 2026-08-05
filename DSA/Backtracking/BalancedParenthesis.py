def generate_parentheses(n, open_count=0, close_count=0, current=""):
    if len(current) == 2 * n:
        print(current)
        return

    if open_count < n:
        generate_parentheses(n, open_count + 1, close_count, current + "(")

    if close_count < open_count:
        generate_parentheses(n, open_count, close_count + 1, current + ")")

generate_parentheses(3)
    